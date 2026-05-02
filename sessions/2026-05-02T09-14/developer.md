# 💻 Developer — Make.com 내 Google Sheets → ChatGPT → Notion 자동화 시나리오 구축 가능성 및 테스트 계획 수립

💻 Developer: 작업 시작합니다.

## ✅ Google Sheets → ChatGPT → Notion 자동화 시나리오 구축 가능성 및 테스트 계획

### 🔧 구축 개요

**목표:**  
Google Sheets에 입력된 단어 목록을 ChatGPT를 통해 영어 학습용 콘텐츠(예: 발음, 뜻, 예문 포함)로 변환하고, 그 결과를 Notion 데이터베이스에 자동 저장하는 워크플로우 구축

**사용 도구:**  
- Google Sheets (입력)  
- ChatGPT (처리)  
- Notion (저장)  
- Make.com (자동화 연결)

---

### ⚙️ 자동화 시나리오 설계

#### 1. 트리거 (Trigger)  
**서비스:** Google Sheets  
**조건:** 새로운 행(row)이 시트에 추가되면 실행  

#### 2. 액션 1 (Action 1): ChatGPT API 호출  
**서비스:** ChatGPT (Make.com 내 OpenAI 모듈 사용)  
**입력:** Google Sheets에서 가져온 단어  
**Prompt 예시:**  
```text
Please provide the pronunciation, Korean meaning, and one example sentence for the following English word: "{word}". Format it as JSON with keys: "pronunciation", "meaning", "example".
```

**출력 예시 (JSON):**  
```json
{
  "pronunciation": "/ˈæpl/",
  "meaning": "사과",
  "example": "I ate an apple for breakfast."
}
```

#### 3. 액션 2 (Action 2): Notion DB에 저장  
**서비스:** Notion  
**입력:** ChatGPT 응답 JSON 및 원래 단어  
**필드 구성 예시:**  
| Word   | Pronunciation | Meaning | Example                     |
|--------|---------------|---------|-----------------------------|
| apple  | /ˈæpl/        | 사과    | I ate an apple for breakfast. |

---

### 📦 필요 준비물

1. **Google Sheets**
   - 시트에 `Word` 열이 존재해야 함
   - Make.com에 시트 접근 권한 부여

2. **ChatGPT API (via Make.com)**
   - OpenAI API Key 필요 (무료/유료 상관없이 키 발급 필요)
   - Make 시나리오 내 OpenAI 모듈 활성화

3. **Notion**
   - 저장할 데이터베이스 사전 생성 (`Word`, `Pronunciation`, `Meaning`, `Example`)
   - Notion API 통합 설정 및 Make.com에 연결

---

### 🧪 테스트 계획

#### Step 1: 샘플 데이터 입력
- Google Sheet에 단어 3개 수동 입력  
  예: `apple`, `banana`, `cat`

#### Step 2: Make 시나리오 실행
- 시나리오 수동 실행 혹은 자동 트리거 작동 여부 확인

#### Step 3: Notion DB 확인
- 각 단어별로 아래 정보가 정확히 저장되었는지 확인:
  - 발음(pronunciation)  
  - 뜻(meaning)  
  - 예문(example)

#### Step 4: 오류 대응
- ChatGPT 응답 형식이 잘못된 경우 → JSON 파싱 실패 가능성 → 기본 fallback 메시지 설정  
- API 제한 시 → 대기 후 재시도 로직 또는 알림 설정

---

### ⏱️ 예상 구축 시간

| 단계 | 소요 시간 |
|------|-----------|
| Google Sheets/Notion 설정 | 10분 |
| Make 시나리오 구축 | 20분 |
| ChatGPT API 테스트 | 15분 |
| 전체 시험 및 수정 | 15분 |
| **총** | **약 1시간** |

---

### ✅ 결론

- **무료 플랜 내에서도 Google Sheets → ChatGPT → Notion 자동화 시나리오 구축 가능함**  
- Make.com 무료 플랜의 1000회/월 실행 한도 내에서 충분히 운용 가능  
- 초급 영어 단어 기반 콘텐츠 자동 생성에 활용 가능하며, 향후 자동 유튜브 스크립트 생성 파이프라인 확장 가능

📝 다음 단계 제안:  
Google Sheets와 Notion DB 템플릿 생성 후 Make 시나리오 구축을 위한 샘플 시트 및 DB 구조를 먼저 정의하겠습니다.
