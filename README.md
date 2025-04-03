# IFITV (Intelligent FIT TV)

맞춤형 IPTV 채널 추천 시스템
사용자 성별/연령대/선호 장르 기반의 콘텐츠 추천 웹 서비스입니다.

---

## ✅ 현재 개발 버전

> 📅 2025.04.03 기준  
> `Flask create_app 패턴 + DB 마이그레이션 완료`

### 💼 구현된 기능

-  Flask 애플리케이션 구조 설정 (create_app 패턴)
-  Blueprint 분리 (`main_views`)
-  SQLite 연동 + SQLAlchemy ORM
-  `UserProfile` 모델 정의
-  사용자 입력(성별, 연령대, 선호 장르/채널) 저장
-  콘텐츠 추천 결과 페이지 출력 (`result.html`)
-  `flask db migrate`, `flask db upgrade` 기반 마이그레이션 정상 작동

---

## 🛠️ 개발 환경

- Python 3.10
- Flask
- Flask-Migrate
- Flask-SQLAlchemy
- SQLite
- VSCode + Windows

---

## 📁 프로젝트 구조

```
ifitv_project/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── recommend.py
│   ├── views/
│   │   ├── __init__.py
│   │   └── main_views.py
│   └── templates/
│       ├── index.html
│       └── result.html
├── config.py
├── extensions.py
├── run.py
├── migrations/
└── ifitv.db
```

---

## ✨ 앞으로 구현할 기능 (To-do)

- [ ] 추천 알고리즘 개선 (장르 유사도 등)
- [ ] 손 모양 제스처 인식 + 자동 로그인
- [ ] 사용자 추천 이력 조회
- [ ] 로그인/회원가입 기능
- [ ] 관리자 전용 페이지

