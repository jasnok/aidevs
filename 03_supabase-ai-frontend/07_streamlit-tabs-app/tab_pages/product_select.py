"""데이터베이스조회 탭입니다."""

import httpx
import streamlit as st
import pandas as pd

API_BASE_URL = "http://127.0.0.1:8000"  # 프론트엔드가 호출할 백엔드 서버의 기본 주소를 한 곳에서 관리합니다.

@st.dialog("삭제")
def show_del(p:dict) -> None:
    st.info("Delete")
    st.write(f"{p['name']}을 삭제 하시겠습니까?")

@st.dialog("수정")
def show_up(p:dict) -> None:
    st.info("Update")



def product_select() -> None:
    """mock 테이블을 선택하고 데이터를 확인합니다."""

    st.subheader("product 조회")
    st.caption("product 테이블을 선택하고 데이터를 확인합니다.")

    with st.spinner("데이터 요청"):
        response = httpx.get(f"{API_BASE_URL}/product/getall", timeout= 10.0)
    if response.status_code == 200:
        result = response.json()

        # df = pd.DataFrame(result)
        # # st.table(df)
        # st.dataframe(df)

        if not result:
            st.info("Product 가 없습니다.")
        for p in result:
            with st.container(border=True):
                product_col, button_col = st.columns([3,1])
                with product_col:
                    st.write(p["id"])
                    st.write(p["name"])
                    st.write(f"{p['price']}원")
                with button_col:
                    if st.button("삭제", key=f"del_{p['id']}"):
                        show_del(p)
                    if st.button("수정", key=f"up_{p['id']}"):
                        show_up(p)
    else:
        st.warning("Fail")