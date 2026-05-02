# ✍️ Writer — 자동화된 스크립트 생성을 위한 표준 프롬프트 템플릿 재검토 및 최적화

✍️ Writer: 작업 시작합니다.

## 📘 자동화된 스크립트 생성을 위한 표준 프롬프트 템플릿 최적화

아래는 영어 학습용 숏폼 콘텐츠(예: 단어 30개 기반) 자동 생성을 위한 **표준 프롬프트 템플릿**입니다.  
ChatGPT, DeepL, 또는 기타 언어 처리 AI와 연동하여 **반복적이고 일관된 콘텐츠 제작**을 가능하게 합니다.

---

### 🎯 프롬프트 템플릿 (영어 단어 학습형 콘텐츠 기준)

```text
You are a professional English teacher creating educational short-form content for beginner learners.

Task:
Create a learning script for the given English word that includes:

1. Pronunciation (in IPA format)
2. Korean meaning
3. One simple example sentence in English
4. One simple example sentence in Korean

Output must be structured in the following JSON format:

{
  "word": "[English word]",
  "pronunciation": "[IPA pronunciation]",
  "meaning_ko": "[Korean meaning]",
  "example_en": "[Example sentence in English]",
  "example_ko": "[Example sentence in Korean]"
}

Use this input word: {INPUT_WORD}
```

---

### 🛠️ 프롬프트 활용 예시 (입력: apple)

```json
{
  "word": "apple",
  "pronunciation": "/ˈæpl/",
  "meaning_ko": "사과",
  "example_en": "I ate an apple for breakfast.",
  "example_ko": "나는 아침으로 사과를 먹었다."
}
```

---

### 🔄 자동화 연동 시 유의사항

1. **변수 치환**: `{INPUT_WORD}` 부분은 Google Sheets 등 외부 소스에서 동적으로 주입
2. **JSON 출력 강제**: 파싱 안정성을 위해 반드시 JSON 형태 반환 지시
3. **톤 유지**: "초급 학습자 대상", "친근하고 격식 없는 설명" 톤 유지

---

### 🧪 테스트 시나리오 예시

| 단계 | 입력 소스       | 처리 도구     | 출력 형태         | 목적                          |
|------|------------------|----------------|--------------------|-------------------------------|
| 1    | Google Sheets    | Make.com       | ChatGPT Prompt     | 단어별 맞춤형 요청 전달      |
| 2    | 단어 리스트       | ChatGPT        | JSON               | 의미/발음/예문 생성          |
| 3    | JSON             | Make.com       | Notion DB 저장     | 자동 아카이빙 및 콘텐츠 관리 |

---

📝 다음 단계 제안: 위 프롬프트를 기반으로 실제 Google Sheets ↔ ChatGPT ↔ Notion 연동 시나리오를 Make.com으로 테스트 구축 및 검증 진행
