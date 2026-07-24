# 03_pizza.py
import streamlit as st

def init_state():
    if "pizza" not in st.session_state:
            st.session_state.pizza = ""
    if "dough" not in st.session_state:
        st.session_state.dough = ""
    if "cheeze" not in st.session_state:
        st.session_state.cheeze = ""
    if "topping" not in st.session_state:
        st.session_state.topping = ""

def clear_state():
    st.session_state.dough = ""
    st.session_state.cheeze = ""
    st.session_state.topping = ""

init_state()

def make_p1():
    st.toast("P1 피자 만듭니다.")
    st.session_state.pizza = "Pizza1"
    st.session_state.dough = "p1도우"
    st.session_state.cheeze = "p1치즈"
    st.session_state.topping = "p1토핑"
def make_p2():
    st.toast("P2 피자 만듭니다.")
    st.session_state.pizza = "Pizza2"
    st.session_state.dough = "p2도우"
    st.session_state.cheeze = "p2치즈"
    st.session_state.topping = "p2토핑"
def make_p3():
    st.toast("P3 피자 만듭니다.")
    st.session_state.pizza = "Pizza3"
    st.session_state.dough = "p3도우"
    st.session_state.cheeze = "p3치즈"
    st.session_state.topping = "p3토핑"

# ==========================================================================================

st.title("Pizza")
if st.session_state.pizza:
    st.subheader(f"{st.session_state.pizza}")

p1, p2, p3 = st.columns(3)

with p1:
    p1_clicked = st.button("P1", on_click = make_p1)
with p2:
    p2_clicked = st.button("P2", on_click = make_p2)
with p3:
    p3_clicked = st.button("P3", on_click = make_p3)


with st.form("pizza_form"):
    dough = st.text_input("도우 선택", key="dough")
    cheeze = st.text_input("치즈 선택", key="cheeze")
    topping = st.text_input("토핑 선택", key="topping")

    submit, reset = st.columns(2)

    with submit:
        submit_clicked = st.form_submit_button("제출")
    with reset:
        reset_clicked  = st.form_submit_button("초기화", on_click=clear_state)

# ==========================================================================================

if submit_clicked:
    st.subheader(f"당신이 선택한 피자는 {st.session_state.pizza}")
    st.info(f"{dough}, {cheeze} {topping}")