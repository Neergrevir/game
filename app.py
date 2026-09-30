from pathlib import Path
import html
import streamlit as st
import streamlit.components.v1 as components

BASE_DIR = Path(__file__).resolve().parent
GAME_FILE = BASE_DIR / "game" / "game.html"

st.set_page_config(
    page_title="Interactive 3D Project",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    .block-container {padding-top: 1.1rem; padding-bottom: 1rem; max-width: 1600px;}
    [data-testid="stSidebar"] {min-width: 280px;}
    .small-note {font-size: .9rem; opacity: .75;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Three.js Interactive 3D Project")
st.caption("Streamlit이 실행 환경을 담당하고, 실시간 3D 게임 로직은 Three.js가 브라우저 안에서 처리합니다.")

with st.sidebar:
    st.header("실행 설정")
    debug = st.toggle("Debug 표시", value=True)
    player_speed = st.slider("플레이어 최대 속도", 2.0, 10.0, 5.5, 0.5)
    camera_distance = st.slider("카메라 거리", 4.0, 12.0, 7.5, 0.5)
    camera_height = st.slider("카메라 높이", 2.0, 8.0, 4.0, 0.5)
    game_height = st.slider("게임 화면 높이", 560, 900, 720, 20)
    st.divider()
    st.markdown("**조작법**")
    st.markdown("WASD / 방향키 — 이동  \n마우스 드래그 — 카메라 회전  \nE — 상호작용  \nR — 게임 재시작")
    st.info("키 입력이 안 되면 먼저 3D 화면 안을 한 번 클릭하세요.")

if not GAME_FILE.exists():
    st.error(f"게임 파일을 찾을 수 없습니다: {GAME_FILE}")
    st.stop()

try:
    game_html = GAME_FILE.read_text(encoding="utf-8")
except OSError as exc:
    st.error(f"게임 파일을 읽는 중 오류가 발생했습니다: {exc}")
    st.stop()

replacements = {
    "__DEBUG__": "true" if debug else "false",
    "__PLAYER_SPEED__": f"{player_speed:.2f}",
    "__CAMERA_DISTANCE__": f"{camera_distance:.2f}",
    "__CAMERA_HEIGHT__": f"{camera_height:.2f}",
}
for key, value in replacements.items():
    game_html = game_html.replace(key, value)

components.html(game_html, height=game_height, scrolling=False)

with st.expander("이 프로젝트가 어떻게 동작하나요?"):
    st.markdown(
        """
        - **Streamlit**: 실행, 설정 패널, 페이지 레이아웃을 담당합니다.
        - **Three.js**: Scene, Player, Collision, Trigger, Event, Camera, Path, Destination을 담당합니다.
        - 이동은 `deltaTime` 기반이라 프레임 속도에 덜 의존합니다.
        - 충돌은 X/Z 축을 분리해 판정하여 벽을 따라 움직일 수 있게 했습니다.
        - `R`은 페이지 새로고침이 아니라 내부 게임 상태만 초기화합니다.
        """
    )
