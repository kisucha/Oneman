# ✂️ Editor — 스크립트를 기반으로 Piper TTS 나레이션을 생성하고, 썸네일과 결합하여 자막이 포함된 숏폼 영상을 FFmpeg로 조립해주세요. 영상 길이는 60초 이내로 유지합니다.

✂️ Editor: 작업 시작합니다.

## 🎙️ 1. Piper TTS 나레이션 생성

먼저, 스크립트를 기반으로 각 단어별 나레이션을 생성합니다.  
Writer가 제공한 스크립트를 기반으로 `.wav` 파일을 생성합니다.

### 🧾 스크립트 파일 준비 (text/script.txt):

```
Ready to learn?
Hello. /həˈloʊ/. 안녕하세요. Hello, how are you today?
Goodbye. /ˌɡʊdˈbaɪ/. 안녕히 가세요. Goodbye, see you tomorrow!
Yes. /jes/. 네. Yes, I like apples.
No. /noʊ/. 아니요. No, I don't want coffee.
Please. /pliːz/. 제발, 부디. Please sit down.
Thank you. /ˈθæŋk juː/. 고마워요. Thank you for your help.
Sorry. /ˈsɑːri/. 미안해요. Sorry, I'm late.
Excuse me. /ɪkˈskjuːz miː/. 실례합니다. Excuse me, where is the restroom?
Help. /help/. 도움. Can you help me, please?
Water. /ˈwɔːtər/. 물. I need some water.
Food. /fuːd/. 음식. I want to eat food.
Eat. /iːt/. 먹다. Let's eat dinner.
Drink. /drɪŋk/. 마시다. I drink milk every day.
Sleep. /sliːp/. 자다. I sleep at night.
Wake up. /weɪk ʌp/. 일어나다. I wake up at 7 AM.
Go. /ɡoʊ/. 가다. Let’s go to school.
Come. /kʌm/. 오다. Come here, please.
See. /siː/. 보다. I see a bird.
Look. /lʊk/. 보다. Look at that big tree.
Listen. /ˈlɪsən/. 듣다. Listen to the music.
```

### 🗣️ TTS 생성 명령 (Piper TTS 사용)

<run_command>mkdir -p "./assets/audio"</run_command>

<run_command>"C:\piper\piper.exe" --model en_US-lessac-medium --output_dir "./assets/audio" < "./text/script.txt"</run_command>

📝 다음 단계 제안: TTS 생성이 완료되면, 썸네일 이미지와 오디오를 FFmpeg를 통해 조합하여 영상을 제작합니다.

---

## 🖥️ 명령 실행 결과
🖥️ `mkdir -p "./assets/audio"` — ❌ 종료 코드 1
```
���� ���͸� �Ǵ� ���� -p��(��) �̹� �ֽ��ϴ�.
���� ���� ���� �� ���� �߻�: -p.

```

🖥️ `"C:\piper\piper.exe" --model en_US-lessac-medium --output_dir "./assets/audio" <` — ❌ 종료 코드 1
```
������ ��θ� ã�� �� �����ϴ�.

```
