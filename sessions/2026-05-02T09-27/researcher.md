# 🔍 Researcher — Make.com, ChatGPT API, Google Sheets 등 무료 툴 조합의 한계와 대안 확인

🔍 Researcher: 작업 시작합니다.

---

### 🔍 Make.com + ChatGPT API + Google Sheets 무료 툴 조합 한계 분석 및 OLLAMA 활용 가능성 검토

#### ✅ 현재 조합의 한계 요약

| 도구 | 무료 플랜 제한 | 실제 활용 이슈 |
|------|----------------|----------------|
| **Make.com** | - 매월 1,000 operations<br>- 최대 5개 시나리오<br>- 1시간당 1 trigger 제한 | - 복잡한 자동화 구성 불가<br>- 유튜브 콘텐츠 스케줄링 등 실시간 처리 어려움 |
| **ChatGPT API (Free)** | - 공식적으로 유료 API만 제공<br>- 무인 사용 불가<br>- Rate limit 엄격 | - 자동화 흐름에 직접 통합 불가능<br>- 테스트용으로만 사용 가능 |
| **Google Sheets** | - Apps Script 하루 90분 실행 제한<br>- 동시 접근 문제 발생 가능 | - 자동화 속도 저하<br>- 실시간 반응형 처리 불가 |

#### ⚠️ 조합 활용 시 발생할 수 있는 문제

- **동시성 문제**: Google Apps Script는 하루 90분만 실행 가능하며, 동시에 여러 작업 처리 어려움  
- **유료 API 의존**: ChatGPT는 무인 자동화에 부적합하여 대체 AI 필요  
- **운영 복잡성 증가**: Make.com 무료 플랜은 다단계 자동화 불가 → 봇 구조 단순화 요구  

---

### 🧠 대안: 로컬 LLM 활용 – OLLAMA

#### ✅ OLLAMA 장점

- **무료/오픈소스**: 비용 없이 LLM 활용 가능  
- **로컬 실행**: API 의존 없이 자체 서버 또는 PC에서 작동  
- **맞춤형 프롬프트**: JSON 포맷 기반 자동화에 최적화 가능  
- **속도 제어 가능**: Google Apps Script ↔ OLLAMA 간 로컬 통신 → 지연 최소화  

#### 🔄 활용 방안 예시

| 용도 | 기존 툴 | OLLAMA 도입 시 변경 방안 |
|------|--------|--------------------------|
| 콘텐츠 생성 | ChatGPT API (유료) | 로컬에서 OLLAMA 실행 후 자동 전달 |
| 스크립트 요약 | 수작업 or 외부 API | OLLAMA로 자동 요약 처리 |
| 자동화 흐름 | Make.com + ChatGPT | Make + Google Apps Script + OLLAMA 조합 |

#### 🛠 기술 구현 예시

```javascript
// Google Apps Script에서 OLLAMA API 호출 예제 (로컬 서버 가정)
function callOllama(prompt) {
  const url = "http://localhost:11434/api/generate";
  const payload = {
    model: "llama3",
    prompt: prompt,
    stream: false
  };

  const options = {
    method: "POST",
    contentType: "application/json",
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const result = JSON.parse(response.getContentText());
  return result.response;
}
```

#### 📉 단점 및 고려사항

- **로컬 서버 필요**: PC 또는 서버가 항상 켜져 있어야 함  
- **성능 제한**: CPU/GPU 사양에 따라 응답 속도 저하  
- **초기 설정 필요**: 모델 다운로드, PATH 설정, API 포트 열기 등  

---

### 📊 결론 및 추천

| 항목 | 판단 | 설명 |
|------|------|------|
| **무료 툴 조합 한계** | ⚠️ 심각함 | ChatGPT API 무인화 불가, Make.com 무료는 기능 제한 많음 |
| **OLLAMA 활용 가능성** | ✅ 매우 높음 | 로컬 LLM은 자동화 흐름에서 안정성과 유연성 제공 |
| **추천 방향** | 🔧 조합형 자동화 | Make (무료) + Google Sheets (Apps Script) + OLLAMA (로컬) |

---

📝 다음 단계 제안:  
OLLAMA 설치 및 테스트용 Google Apps Script 샘플 코드 작성 후, Make 시나리오와 연동 가능한지 PoC 진행하기
