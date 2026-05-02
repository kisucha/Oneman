# 💻 Developer — Make.com 무료 플랜 내에서 ChatGPT API 기반 자동화 파이프라인 구축 가능성 평가 및 제한사항 정리

💻 Developer: 작업 시작합니다.

---

## ✅ Make.com 무료 플랜 내 ChatGPT API 기반 자동화 파이프라인 구축 가능성 및 제한사항 정리

### 🔍 1. Make.com 무료 플랜 기능 요약 및 제한사항

| 항목 | 무료 플랜 제공 여부 | 제한사항 |
|------|---------------------|----------|
| 시나리오 개수 | 최대 **5개** | 동시에 여러 시나리오 운영 불가 |
| 월 실행 횟수 | **1,000회/월** | 초과 시 차단 |
| 동시 실행 | ❌ 불가능 | 하나의 시나리오만 실행 가능 |
| ChatGPT 모듈 연동 | ✅ 가능 | OpenAI 계정 API 키 필요 |
| 외부 서비스 연동 | ✅ 가능 | Google Sheets, Notion, Slack 등 대부분 무료 연동 가능 |
| 트리거/액션 조합 | ✅ 가능 | 제한 없음 (실행 횟수 제한 내에서) |

📌 *결론*:  
**Make.com 무료 플랜에서도 ChatGPT 기반 자동화 파이프라인 구축이 충분히 가능함**

---

### 🛠️ 2. ChatGPT 기반 자동화 워크플로우 구성 예시

#### 시나리오: Google Sheets → ChatGPT → YouTube Shorts Script 생성 → Notion 저장

##### Step 1: 입력
- **Google Sheets**: 단어 리스트 (예: Apple, Book, Cat 등)가 정해진 형식으로 입력됨

##### Step 2: 자동 처리
- **Make.com 트리거**: Google Sheets 행 추가 감지
- **ChatGPT 액션**: 입력 단어를 기반으로 "발음 + 뜻"이 담긴 YouTube Shorts 스크립트 생성 요청
- **ChatGPT 프롬프트 예시**:
  ```
  You are an English teacher for Korean beginners. Create a YouTube short script explaining the following word with pronunciation and meaning in Korean.
  Word: {{word}}
  ```

##### Step 3: 출력
- **Notion DB 저장**: 생성된 스크립트 자동 저장
- **선택**: Google Docs로 자동 저장 가능 (협업용)

---

### ⚠️ 3. 제한사항 및 대응 방안

| 제한사항 | 설명 | 대응 방안 |
|----------|------|------------|
| 월 1,000회 실행 제한 | 단어 1개 = 1회 실행 기준, 최대 1,000개 단어 처리 가능 | 주 1회 배치 방식으로 처리 계획 |
| ChatGPT API 비용 발생 | OpenAI API는 별도 과금 구조 | 무료 크레딧 활용, 또는 GPT-3.5-turbo 등 저비용 모델 사용 |
| 동시 실행 불가 | 여러 시나리오 동시에 실행 불가 | 작업 시간 겹치지 않도록 스케줄링 |

---

### 📦 4. 각 파트별 무료 도구 및 운용 방법 정리

| 파트 | 도구명 | 무료 여부 | 운용 방법 |
|------|--------|-----------|------------|
| 입력 관리 | Google Sheets | ✅ 무료 | 단어 리스트 입력 (Make.com 트리거 연동) |
| AI 스크립트 생성 | ChatGPT (OpenAI API) | ⚠️ 무료 크레딧 제공 | GPT-3.5-turbo 모델 사용, Make.com 내 OpenAI 모듈 연동 |
| 텍스트 편집 | Google Docs | ✅ 무료 | 스크립트 초안 공유 및 공동 편집 |
| 템플릿/일정 관리 | Notion | ✅ 무료 (개인 사용) | 생성된 스크립트 자동 저장, 제작 일정 관리 |
| 영상 편집 | CapCut | ✅ 무료 | 자동 자막, 효과, 음원 적용 |
| 디자인 | Canva | ✅ 무료 (기본 기능) | 썸네일 템플릿 제작 및 재사용 |
| 자동화 워크플로우 | Make.com | ✅ 무료 (기본 기능) | Google Sheets → ChatGPT → Notion 자동화 시나리오 구축 |

---

### 🧪 5. 실제 시나리오 예시 (Make.com 구성 순서)

1. **트리거**: Google Sheets > Watch Rows > 특정 시트의 새로운 행 감지
2. **액션 1**: OpenAI > Create a Completion > 위에서 감지된 단어 기반으로 프롬프트 실행
3. **액션 2**: Notion > Create a Database Item > 생성된 스크립트를 Notion DB에 저장
4. *(선택)* **액션 3**: Google Docs > Create/Update Document > 스크립트 자동 입력

📌 *Tip*:  
프롬프트 내 `{{word}}`, `{{pronunciation}}`, `{{meaning}}` 등의 변수를 활용하면 더 정교한 자동화 가능

---

📝 다음 단계 제안:  
Make.com에서 Google Sheets ↔ ChatGPT ↔ Notion 연동 시나리오를 실제로 구축하고 테스트해보기
