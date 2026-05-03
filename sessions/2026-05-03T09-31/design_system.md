# 🎨 CHK Contents 디자인 시스템 (썸네일 ver.)

## 1. 컬러 팔레트

| 요소 | HEX | 용도 |
|------|-----|------|
| Primary Background | `#E53935` | 썸네일 배경, 주요 시각 요소 |
| Highlight | `#FFD54F` | 단어 박스, 강조 요소 |
| Info Text | `#42A5F5` | 단어 뜻, 세부 정보 |
| Text Base | `#FFFFFF` | 제목, 본문 텍스트 |

---

## 2. 타이포그래피

### 폰트 경로 우선순위

| 폰트 | 위치 | fallback |
|------|------|----------|
| Pretendard Bold | `C:\Windows\Fonts\Pretendard-Bold.ttf` | Helvetica |
| Pretendard Regular | `C:\Windows\Fonts\Pretendard-Regular.ttf` | Arial |

> ⚠️ 폰트 없을 경우 자동으로 Arial 사용

---

## 3. 레이아웃 구조

```
+--------------------------------------+
| [LOGO]                    [제목]     |
|                                      |
|        대표 단어 5개 시각화          |
+--------------------------------------+
```

- 제목 크기: 60pt
- 단어 박스 크기: 120px × 120px
- 여백(Margin): 좌우 80px, 상하 60px

---

## 4. 시각 요소 구성

| 요소 | 스타일 |
|------|-------|
| 제목 | Pretendard Bold, 흰색, 중앙 정렬 |
| 단어 박스 | 노랑 원형 배경, 파랑 텍스트, 아이콘 포함 |
| 로고 | 우측 상단, 100×40px |
| 전체 해상도 | 1280×720 (유튜브 썸네일 표준) |

---

## 5. 자동화 플로우

1. Researcher에서 단어 5개 추출
2. 단어명+아이콘으로 단어 박스 생성
3. ImageMagick으로 조합 → `thumbnail.png` 저장