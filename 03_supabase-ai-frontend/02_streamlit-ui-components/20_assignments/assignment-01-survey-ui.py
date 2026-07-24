# 로그인 화면
# 로그인 성공 시 다양한 컴포넌트를 이용한 설문지를 보여준다.
# 설문 제출 후 설문 화면을 없애고 결과를 출력한다.
# 로그인 실패 시 로그인 화면에서 오류 메시지를 보여준다.

# assignment-01-survey-ui.py

import streamlit as st


# 선언 ======================================================================

# 로그인 상태
if "login" not in st.session_state:
    st.session_state.login = False

# 설문 완료 상태
if "survey_complete" not in st.session_state:
    st.session_state.survey_complete = False

# 설문 결과 초기값
if "survey_name" not in st.session_state:
    st.session_state.survey_name = ""

if "survey_age" not in st.session_state:
    st.session_state.survey_age = 20

if "survey_intro" not in st.session_state:
    st.session_state.survey_intro = ""

if "survey_interest" not in st.session_state:
    st.session_state.survey_interest = "Python"

if "survey_skills" not in st.session_state:
    st.session_state.survey_skills = []

if "survey_agree" not in st.session_state:
    st.session_state.survey_agree = False

if "survey_score" not in st.session_state:
    st.session_state.survey_score = 5


# 각 화면에서 사용할 버튼의 기본값
login_button = False
survey_submit = False
rewrite_button = False
logout_button = False


# 화면 ======================================================================

# 1. 로그인 화면
if st.session_state.login == False:
    st.title("로그인 화면")

    input_id = st.text_input("아이디")
    input_pwd = st.text_input("비밀번호", type="password")

    login_button = st.button("로그인")


# 2. 설문지 화면
elif st.session_state.survey_complete == False:
    st.title("설문지 화면")

    survey_name = st.text_input("이름을 입력하세요.")

    survey_age = st.number_input(
        "나이를 입력하세요.",
        min_value=1,
        max_value=100,
        value=20
    )

    survey_intro = st.text_area(
        "자기소개를 작성하세요."
    )

    survey_interest = st.selectbox(
        "가장 관심 있는 분야를 선택하세요.",
        ["Python", "FastAPI", "Streamlit", "AI"]
    )

    survey_skills = st.multiselect(
        "배워본 기술을 모두 선택하세요.",
        ["Python", "Git", "FastAPI", "Streamlit", "Supabase"]
    )

    survey_agree = st.checkbox(
        "설문 내용 제출에 동의합니다."
    )

    survey_score = st.slider(
        "오늘 수업의 이해도를 선택하세요.",
        min_value=0,
        max_value=10,
        value=5
    )

    survey_submit = st.button("설문 제출")


# 3. 결과 화면
else:
    st.title("설문 결과")

    st.subheader("입력한 정보")

    st.write(f"이름: {st.session_state.survey_name}")
    st.write(f"나이: {st.session_state.survey_age}")
    st.write(f"자기소개: {st.session_state.survey_intro}")
    st.write(f"관심 분야: {st.session_state.survey_interest}")

    # 선택한 기술이 있는 경우 문자열로 연결해서 출력
    if st.session_state.survey_skills:
        skills_text = ", ".join(st.session_state.survey_skills)
    else:
        skills_text = "선택한 기술이 없습니다."

    st.write(f"배워본 기술: {skills_text}")
    st.write(
        f"제출 동의: "
        f"{'동의' if st.session_state.survey_agree else '미동의'}"
    )
    st.write(f"수업 이해도: {st.session_state.survey_score}/10")

    rewrite_button = st.button("설문 다시 작성")
    logout_button = st.button("로그아웃")


# 코드 ======================================================================

# 로그인 처리
if login_button:
    if input_id == "id01" and input_pwd == "pwd01":
        st.session_state.login = True
        st.rerun()
    else:
        st.error("아이디 또는 비밀번호가 올바르지 않습니다.")


# 설문 제출 처리
if survey_submit:
    # 이름 앞뒤의 불필요한 공백 제거
    survey_name = survey_name.strip()

    if survey_name == "":
        st.warning("이름을 입력해 주세요.")

    elif survey_agree == False:
        st.warning("설문 내용 제출에 동의해 주세요.")

    else:
        # 설문 결과를 session_state에 저장
        st.session_state.survey_name = survey_name
        st.session_state.survey_age = survey_age
        st.session_state.survey_intro = survey_intro
        st.session_state.survey_interest = survey_interest
        st.session_state.survey_skills = survey_skills
        st.session_state.survey_agree = survey_agree
        st.session_state.survey_score = survey_score

        # 설문 완료 상태로 변경
        st.session_state.survey_complete = True
        st.rerun()


# 설문 다시 작성
if rewrite_button:
    st.session_state.survey_complete = False
    st.rerun()


# 로그아웃
if logout_button:
    st.session_state.login = False
    st.session_state.survey_complete = False

    # 이전 설문 결과 초기화
    st.session_state.survey_name = ""
    st.session_state.survey_age = 20
    st.session_state.survey_intro = ""
    st.session_state.survey_interest = "Python"
    st.session_state.survey_skills = []
    st.session_state.survey_agree = False
    st.session_state.survey_score = 5

    st.rerun()