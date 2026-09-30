# Three.js + Streamlit Interactive 3D Project

## 가장 쉬운 실행 방법

1. 이 폴더를 VS Code로 엽니다.
2. VS Code 상단 메뉴에서 `터미널 > 새 터미널`을 엽니다.
3. 아래 명령을 순서대로 실행합니다.

```bash
pip install -r requirements.txt
streamlit run app.py
```

4. 브라우저가 자동으로 열립니다. 열리지 않으면 터미널에 표시되는 `http://localhost:8501` 주소를 클릭합니다.
5. 3D 화면 안을 한 번 클릭한 뒤 WASD 또는 방향키로 움직입니다.

## 조작법

- W / ↑ : 전진
- S / ↓ : 후진
- A / ← : 좌측 이동
- D / → : 우측 이동
- 마우스 드래그 : 카메라 회전
- E : 상호작용
- R : 내부 상태 재시작

## 구조

```text
threejs-streamlit-3d/
├── app.py
├── requirements.txt
├── README.md
└── game/
    └── game.html
```

`app.py`가 Streamlit UI와 실행 환경을 만들고, `game/game.html` 안에서 Three.js 게임이 실행됩니다.
Three.js는 CDN을 사용하므로 최초 실행 시 인터넷 연결이 필요합니다.


## WebGL 호환성
이 버전은 Three.js r162를 사용하여 WebGL 1과 WebGL 2 환경 모두에서 실행 가능성을 높였습니다. 최신 Three.js r163 이상은 WebGL 2만 지원합니다.
