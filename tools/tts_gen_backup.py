# TTS 나레이션 생성기 v2
# 역할: script.txt 줄 단위 파싱 → (pause X) 는 무음, 텍스트는 TTS 변환
# 출력: narration.wav + narration_timings.json (slide_gen.py 동기화용)
import re, sys, wave, json
import numpy as np
from kokoro_onnx import Kokoro

# ─── 일시정지 패턴 (세 가지 표기 모두 지원) ────────────────────────────────
# (pause 2 seconds)  /  (pause 2 second)
# ···2s···
# [PAUSE:2]
PAUSE_RE = re.compile(
    r'^\s*(?:'
    r'\(pause\s+([\d.]+)\s+seconds?\)'
    r'|···([\d.]+)s···'
    r'|\[PAUSE:([\d.]+)\]'
    r')\s*$',
    re.IGNORECASE
)

def parse_pause(line: str) -> float | None:
    """일시정지 줄이면 초(float) 반환, 아니면 None"""
    m = PAUSE_RE.match(line)
    if not m:
        return None
    return float(next(g for g in m.groups() if g is not None))

# ─── 인수 파싱 ────────────────────────────────────────────────────────────
script_path = sys.argv[1]   # script.txt 경로
out_path    = sys.argv[2]   # narration.wav 출력 경로

# ─── kokoro 초기화 ────────────────────────────────────────────────────────
k = Kokoro(
    r'C:\Develop\speaking\kokoro_models\kokoro-v0_19.onnx',
    r'C:\Develop\speaking\kokoro_models\voices.bin'
)

SR    = 24000   # kokoro 기본 샘플레이트 (실제 sr로 갱신됨)
SPEED = 0.7     # 나레이션 속도 — 0.7 = 30% 감속, 1.0 = 기본 속도

# ─── 줄 단위 처리 ─────────────────────────────────────────────────────────
lines    = open(script_path, encoding='utf-8').read().splitlines()
segments: list[np.ndarray] = []   # 오디오 세그먼트 목록
timings:  list[dict]       = []   # slide_gen.py 타이밍 동기화 데이터

for line in lines:
    text = line.strip()
    if not text:
        continue  # 빈 줄 무시

    pause_sec = parse_pause(text)

    if pause_sec is not None:
        # ── 일시정지: 무음 샘플 삽입 ──────────────────────────────────────
        silence = np.zeros(int(SR * pause_sec), dtype=np.int16)
        segments.append(silence)
        timings.append({'type': 'pause', 'duration': pause_sec})
        print(f'  [무음] {pause_sec:.1f}초')
    else:
        # ── 텍스트: TTS 변환 ──────────────────────────────────────────────
        audio, sr = k.create(text, voice='af', speed=SPEED, lang='en-us')
        SR = sr  # 실제 샘플레이트로 갱신
        samples = (np.clip(audio, -1, 1) * 32767).astype(np.int16)
        segments.append(samples)
        dur = len(samples) / SR
        timings.append({'type': 'text', 'text': text, 'duration': dur})
        print(f'  [TTS] {text[:60]}  ({dur:.2f}초)')

if not segments:
    print('오류: 생성할 오디오 없음')
    sys.exit(1)

# ─── WAV 저장 ─────────────────────────────────────────────────────────────
combined = np.concatenate(segments)
with wave.open(out_path, 'w') as f:
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(SR)
    f.writeframes(combined.tobytes())

# ─── 타이밍 JSON 저장 (slide_gen.py 가 사용) ─────────────────────────────
timings_path = out_path.replace('.wav', '_timings.json')
with open(timings_path, 'w', encoding='utf-8') as f:
    json.dump(timings, f, ensure_ascii=False, indent=2)

total = len(combined) / SR
print(f'완료: {out_path}  총 {total:.1f}초')
print(f'타이밍: {timings_path}')
