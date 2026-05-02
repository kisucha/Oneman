# ✍️ Writer — 로컬 LLM 활용 시 프롬프트 템플릿 최적화 방안 제안

✍️ Writer: 작업 시작합니다.

---

## 📌 로컬 LLM(Ollama) 활용 시 프롬프트 템플릿 최적화 방안

### 🎯 목적  
CHK Contents의 영상 콘텐츠 제작 과정에서 AI 스크립트 자동 생성 및 요약을 효율화하기 위해, **로컬 LLM**(Ollama) 기반의 **표준 프롬프트 템플릿**을 설계하고 최적화하는 방안을 제안합니다.

---

## ✅ 1. 로컬 LLM 활용 시 프롬프트 템플릿 설계 원칙

| 원칙 | 설명 |
|------|------|
| **명확한 역할 부여** | AI는 “콘텐츠 기획자”, “스크립트 작성자” 등의 역할로 행동하도록 지시 |
| **JSON 입력/출력 구조** | 자동화와 연동을 위해 JSON 형식 기반 입출력 통일 |
| **반복성 보장** | 동일 입력에 대해 일관된 출력을 얻도록 프롬프트 구성 |
| **요청 구조 단순화** | 복잡한 요청은 단계별로 분할하여 처리 |

---

## 🧩 2. 기본 프롬프트 템플릿 예시 (JSON 기반)

### 📌 [템플릿 1] 단어 기반 숏폼 콘텐츠 생성
```json
{
  "task": "create_short_video_script",
  "input": {
    "words": ["apple", "book", "cat", "dog"],
    "tone": "beginner-friendly",
    "style": "repetitive and visual"
  },
  "prompt": "You are an English content creator for beginners. Based on the list of words provided, create a short script that includes pronunciation, meaning, and example sentence for each word in a repetitive and visual-friendly format."
}
```

### 📌 [템플릿 2] 영상 오프닝 문구 생성
```json
{
  "task": "generate_opening_line",
  "input": {
    "theme": "daily vocabulary boost",
    "mood": "light & fun"
  },
  "prompt": "Create one catchy and friendly opening line for a YouTube video aimed at beginner learners of English. The theme is daily vocabulary improvement with a light and fun tone. Example: 'Ready to learn?'"
}
```

### 📌 [템플릿 3] 스크립트 요약 생성
```json
{
  "task": "summarize_script",
  "input": {
    "script_text": "[스크립트 전문]",
    "length": "short"
  },
  "prompt": "Summarize the following YouTube script into a short description suitable for a thumbnail caption or metadata. Keep it under 50 characters if possible."
}
```

---

## 🛠 3. 로컬 LLM 연동 자동화 구조 제안

### ▶ Google Apps Script ↔ OLLAMA ↔ Make.com

1. **Google Sheets**: 콘텐츠 키워드/단어 입력
2. **Apps Script**: JSON 템플릿 기반 OLLAMA 호출
3. **OLLAMA**: LLM 기반 스크립트 생성
4. **Make.com**: 결과 데이터를 YouTube Studio / Canva 등으로 전달

### 🔄 예시 코드 (Apps Script 내 OLLAMA 호출)
```javascript
function generateScriptFromTemplate(templateObj) {
  const url = "http://localhost:11434/api/generate";
  const payload = {
    model: "llama3",
    prompt: templateObj.prompt,
    stream: false
  };

  const options = {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    payload: JSON.stringify(payload)
  };

  const res = UrlFetchApp.fetch(url, options);
  const result = JSON.parse(res.getContentText());

  return result.response.trim();
}
```

---

## 📈 4. 템플릿 최적화를 위한 테스트 방법

| 테스트 항목 | 방법 | 목적 |
|------------|------|------|
| 반복성 확인 | 동일 입력으로 5회 이상 실행 | 동일 출력 확인 |
| 정확도 측정 | 생성 결과 vs 수작업 비교 | 유효성 검증 |
| 응답 속도 | 평균 응답 시간 측정 | 성능 벤치마크 |
| LLM 모델 비교 | Llama3 vs Mistral | 최적 모델 선정 |

---

## 🧠 5. 추가 최적화 아이디어

- **프롬프트 캐싱**: 자주 사용하는 요청은 캐시하여 재사용
- **멀티모달 확장**: 이미지 입력도 받을 수 있도록 템플릿 확장 (향후)
- **자동 번역 포함**: 생성된 영어 스크립트 자동 한국어 번역 포함 옵션

---

📝 다음 단계 제안:  
**Developer 에이전트에게 OLLAMA ↔ Google Apps Script 연동 샘플 코드 구현 요청**  
→ 이후 Make.com 자동화 테스트에 활용 예정
