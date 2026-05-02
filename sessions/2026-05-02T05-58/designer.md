# 🎨 Designer — Canva, Figma, Adobe Express 등 썸네일 템플릿 제작 및 디자인 시스템 구축에 적합한 툴 검토

🎨 Designer: 작업 시작합니다.

### 📊 썸네일 템플릿 및 디자인 시스템 구축을 위한 툴 검토 보고서

디자인 시스템의 핵심은 **'일관성(Consistency)'**과 **'효율성(Efficiency)'**입니다. 1인 기업 및 소규모 제작 환경에 최적화된 툴 선정 및 워크플로우를 제안합니다.

#### 1. 툴별 비교 분석 (Design System vs. Production)

| 구분 | **Figma (설계/시스템)** | **Canva (제작/템플릿)** | **Adobe Express (중간)** |
| :--- | :--- | :--- | :--- |
| **주요 역할** | **디자인 시스템 구축** (Rule Making) | **콘텐츠 양산** (Template Application) | 그래픽 소스 활용 및 편집 |
| **핵심 강점** | 컴포넌트화, 폰트/컬로 가이드 정밀화 | 템플릿 복제, 빠른 텍스트/이미지 교체 | Adobe 스톡 리소스 연동 |
| **난이도** | 높음 (전문가적 접근 필요) | 매우 낮음 (누구나 가능) | 보통 |
| **추천 용도** | 브랜드 가이드라인, 레이아웃 설계 | 썸네일/숏폼 템플릿 실제 제작 | 상업용 스톡 활용 시 |

---

#### 2. 최적의 워크플로우 제안: [Hybrid Strategy]
단일 툴 사용보다 **'Figma(설계) $\rightarrow$ Canva(생산)'**의 이원화 전략을 추천합니다.

**[Phase 1] Design System 구축 (Figma 활용)**
- **목적:** 브랜드의 뼈대를 만듭니다. 툴을 바꾸더라도 흔들리지 않는 기준을 만듭니다.
- **작업 내용:**
    - **Color Palette:** 파랑/노랑 기반의 HEX 코드 정의 (Primary/Secondary/Accent).
    - **Typography:** 'Pretendard' 폰트의 위계(Bold/Medium/Regular) 설정.
    - **Layout Grid:** 썸네일용 16:9 레이아웃 및 숏폼 9:16 안전 영역(Safe Zone) 정의.
    - **Component:** 로고, 아이콘, 텍스트 박스 스타일 정의.

**[Phase 2] 템플릿 양산 (Canva 활용)**
- **목적:** 일상적인 숏폼/썸네일 제작 시간을 최소화합니다.
- **작업 내용:**
    - Figma에서 확정된 컬러와 폰트를 Canva 브랜드 키트(Brand Kit)에 등록.
    - 텍스트 내용만 바꾸면 바로 사용 가능한 **'Master Template'** 3종 제작.
    - 1) 숏폼 텍스트 강조형 템플스트, 2) 썸네일 헤드라인 템플릿, 3) 인트로/아웃트로 템플릿.

---

#### 3. 디자인 시스템(Design System) 구성 요소 리스트
시스템 구축 시 반드시 포함해야 할 가이드라인입니다.

1.  **Color System:** 
    - `Primary Blue`: #0000FF (예시)
    - `Secondary Yellow`: #FFFF00 (예시)
    - `Text Black/White`: 가독성을 위한 대비색
2.  **Typography System:**
    - `Headline`: Pretendard Bold (주요 키워드)
    - `Sub-headline`: Pretend라 Medium (부연 설명)
    - `Body`: Pretendard Regular (내용)
3.  **Visual Assets:**
    - 숏폼 내 자막 위치 가이드 (상단/하단 여백 확보)
    - 썸네일 내 텍스트 배치 규칙 (좌측/우측/중앙)

📝 다음 단계 제안: 디자인 시스템의 핵심인 'Color Palette(HEX)' 및 'Typography Hierarchy' 초안 정의.
