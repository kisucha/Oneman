import re

# 파일 경로 설정
script_path = "c:\\Oneman Company\\sessions\\2026-05-03T05-37\\script.txt"
tts_script_path = "c:\\Oneman Company\\sessions\\2026-05-03T05-37\\tts_script.txt"

# 스크립트 읽기
with open(script_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 영어 단어 및 예문만 필터링
english_lines = []
for line in lines:
    stripped_line = line.strip()
    # 숫자로 시작하는 라인, 괄호로 시작하는 라인, "Ready to learn?" 라인 제외
    if not re.match(r'^\d+\.', stripped_line) and \
       not stripped_line.startswith('(') and \
       stripped_line.lower() != 'ready to learn?' and \
       stripped_line: # 빈 라인 제외
        # 한글이 포함된 라인 제외 (이번 스크립트에는 없지만 안전장치)
        if not re.search('[가-힣]', stripped_line):
            english_lines.append(stripped_line)

# 필터링된 내용을 tts_script.txt에 저장
with open(tts_script_path, 'w', encoding='utf-8') as f:
    for line in english_lines:
        f.write(line + '\n')

print(f"TTS 스크립트가 생성되었습니다: {tts_script_path}")