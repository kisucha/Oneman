# 슬라이드 영상 생성기 v2
# 역할: script.txt + narration.wav → 슬라이드 PNG 시퀀스 → final.mp4
# 신규: narration_timings.json 로드 시 정확한 타이밍으로 슬라이드 동기화
#       일시정지 줄은 슬라이드 생성 없이 이전 슬라이드 표시 시간으로 흡수
import sys, os, re, json, subprocess, wave, contextlib, textwrap

# ─── 일시정지 패턴 (tts_gen.py 와 동일) ──────────────────────────────────
PAUSE_RE = re.compile(
    r'^\s*(?:'
    r'\(pause\s+([\d.]+)\s+seconds?\)'
    r'|···([\d.]+)s···'
    r'|\[PAUSE:([\d.]+)\]'
    r')\s*$',
    re.IGNORECASE
)

def is_pause(line: str) -> bool:
    return bool(PAUSE_RE.match(line.strip()))

def get_wav_duration(wav_path: str) -> float:
    with contextlib.closing(wave.open(wav_path, 'r')) as f:
        return f.getnframes() / float(f.getframerate())

# ─── 인수 파싱 ────────────────────────────────────────────────────────────
script_path = sys.argv[1]                                    # script.txt
wav_path    = sys.argv[2]                                    # narration.wav
output_mp4  = sys.argv[3]                                    # final.mp4
bg_color    = sys.argv[4] if len(sys.argv) > 4 else '#1a1a2e'
font_color  = sys.argv[5] if len(sys.argv) > 5 else 'white'
font_size   = sys.argv[6] if len(sys.argv) > 6 else '52'

session_dir = os.path.dirname(output_mp4)
slides_dir  = os.path.join(session_dir, 'slides')
os.makedirs(slides_dir, exist_ok=True)

# ─── 슬라이드 이미지 생성 (ImageMagick) ──────────────────────────────────
def make_slide(idx: int, text: str) -> str:
    """텍스트를 PNG 슬라이드로 렌더링, 저장 경로 반환"""
    slide_path = os.path.join(slides_dir, f'slide_{idx:03d}.png')
    wrapped    = '\n'.join(textwrap.wrap(text, width=28))
    cmd = [
        'magick', '-size', '1280x720', f'xc:{bg_color}',
        '-font', 'C:/Windows/Fonts/malgun.ttf',
        '-pointsize', font_size, '-fill', font_color,
        '-gravity', 'center', '-annotate', '0', wrapped, slide_path
    ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(f'슬라이드 {idx} 생성 실패: {r.stderr}')
        sys.exit(1)
    return slide_path

def make_blank_slide(idx: int) -> str:
    """빈(검정) 슬라이드 생성 - 오프닝 일시정지용"""
    slide_path = os.path.join(slides_dir, f'slide_{idx:03d}.png')
    subprocess.run(
        ['magick', '-size', '1280x720', f'xc:{bg_color}', slide_path],
        capture_output=True
    )
    return slide_path

# ─── 슬라이드 + 타이밍 목록 구성 ─────────────────────────────────────────
# slide_entries: [(슬라이드 경로, 표시 시간(초)), ...]
slide_entries: list[tuple[str, float]] = []

timings_path = wav_path.replace('.wav', '_timings.json')

if os.path.exists(timings_path):
    # ── 모드 A: tts_gen.py v2 타이밍 파일 사용 ───────────────────────────
    print(f'타이밍 파일 로드: {timings_path}')
    with open(timings_path, encoding='utf-8') as f:
        timings: list[dict] = json.load(f)

    slide_idx = 0
    for entry in timings:
        if entry['type'] == 'text':
            # 새 슬라이드 생성
            path = make_slide(slide_idx, entry['text'])
            slide_entries.append((path, entry['duration']))
            print(f'  [{slide_idx+1}] "{entry["text"][:40]}"  ({entry["duration"]:.2f}초)')
            slide_idx += 1
        else:
            # 일시정지: 이전 슬라이드 표시 시간 연장
            pause_dur = entry['duration']
            if slide_entries:
                prev_path, prev_dur = slide_entries[-1]
                slide_entries[-1] = (prev_path, prev_dur + pause_dur)
                print(f'  [일시정지 {pause_dur:.1f}초] 이전 슬라이드 연장')
            else:
                # 맨 첫 항목이 일시정지인 경우 - 빈 슬라이드로 처리
                path = make_blank_slide(slide_idx)
                slide_entries.append((path, pause_dur))
                print(f'  [오프닝 일시정지 {pause_dur:.1f}초] 빈 슬라이드')
                slide_idx += 1
else:
    # ── 모드 B: 폴백 — 일시정지 줄 제외 + 균등 분배 ─────────────────────
    print('타이밍 파일 없음 - 폴백 모드 (균등 분배)')
    all_lines   = open(script_path, encoding='utf-8').read().splitlines()
    text_lines  = [l.strip() for l in all_lines if l.strip() and not is_pause(l)]
    if not text_lines:
        print('ERROR: 표시할 텍스트 줄이 없습니다')
        sys.exit(1)
    total_dur  = get_wav_duration(wav_path)
    slide_dur  = total_dur / len(text_lines)
    for i, line in enumerate(text_lines):
        path = make_slide(i, line)
        slide_entries.append((path, slide_dur))
        print(f'  [{i+1}/{len(text_lines)}] {path}')

# ─── concat.txt 생성 (FFmpeg 슬라이드쇼 입력) ────────────────────────────
concat_path = os.path.join(slides_dir, 'concat.txt')
with open(concat_path, 'w', encoding='utf-8') as f:
    for sp, dur in slide_entries:
        # FFmpeg concat demuxer — Windows 경로 역슬래시를 슬래시로 변환
        safe_path = sp.replace('\\', '/')
        f.write(f"file '{safe_path}'\nduration {dur:.3f}\n")
    # 마지막 슬라이드 재기재 (FFmpeg concat 필수)
    f.write(f"file '{slide_entries[-1][0].replace(chr(92), '/')}'\n")

# ─── FFmpeg: 슬라이드쇼 + 오디오 합성 ───────────────────────────────────
r = subprocess.run([
    'ffmpeg', '-y',
    '-f', 'concat', '-safe', '0', '-i', concat_path,
    '-i', wav_path,
    '-c:v', 'libx264', '-tune', 'stillimage',
    '-c:a', 'aac', '-b:a', '192k',
    '-pix_fmt', 'yuv420p', '-shortest',
    output_mp4
], capture_output=True, text=True)

if r.returncode == 0:
    print(f'완료: {output_mp4}')
else:
    print(f'FFmpeg 실패:\n{r.stderr[-800:]}')
    sys.exit(1)
