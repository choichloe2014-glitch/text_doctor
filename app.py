import streamlit as st
import re

st.set_page_config(page_title="Text doctor")

st.title("Text doctor = 정규표현식 기반 텍스트 정보 추출기")


st.subheader("텍스트 입력")
text = st.text_area("여기에 텍스트를 붙여넣으세요")

tab1, tab2, tab3 = st.tabs( ["이메일 추출", "전화번호 추출", "이름 추출"])

with tab1:
    st.subheader(".com / .net 이메일만 추출")

    st.markdown("도메인을 선택하세요.")
    selected_doamains = []
    col1, col2, col3, col4, = st.columns(4)

    with col1:
        if st.checkbox(".com", value=True): selected_doamains.append("com")
    with col2:
        if st.checkbox(".net", value=True): selected_doamains.append("net")
    with col3:
        if st.checkbox(".co.kr", value=True): selected_doamains.append("co.kr")
    with col4:
        if st.checkbox(".org", value=True): selected_doamains.append("org")



    if st.button("이메일 추출", key="email"):
       
        if not selected_doamains:
            st.warning("하나 이상의 더메인을 선택하세요.")
        else:
            # .com , .net, co.kr, org 중 선택한 도메인의 email을 추출
            domain_pattern = "|".join(re.escape(domain) for domain in selected_doamains)
            matches = re.findall(rf"([a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.({domain_pattern}))", text)
            results = [m[0] for m in matches]
            print(results)

            if results:
                st.success(f"총{len(results)}개의 이메일을 찾았습니다.")
                for email in results:
                    st.write(".", email)
            else:
                st.warning("추출된 이메일이 없습니다.")
            
with tab2:
    st.subheader("한국 전화번호 추출")

    if st.button("전화번호 추출", key="phone"):

        # 010-XXXX-XXXX 또는 02-XXX-XXXX 현식만 추출
        phone_numbers = re.findall(r"\b(\d{2,3}[- ]?\d{3,4}[- ]?\d{4})\b", text)
        # phone_number = [m[0] for m in matches]
        # print(phone_number)

        if phone_numbers:
            st.success(f"총{len(phone_numbers)}개의 전화번호를 찾았습니다.")
            for phone in phone_numbers:
                st.write(".", phone)
        else:
            st.warning("추출된 전화번호가 없습니다.")
with tab3:
    st.subheader("이름 추출(영문 이름. 예를 들어, Luke Skywarker)")

    if st.button("이름 추출", key="name"):
       
        name_pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
        names = re.findall(name_pattern, text)

        if names:
            st.success(f"총 {len(names)}개의 이름을 찾았습니다.")
            for name in names:
                st.write(".", name)
        else:
            st.warning("해당 형식의 이름이 없습니다.")
            