import streamlit as st

# 오에에엥이 MBTI별 직업 추천 리스트 만들어봤다!
# 현정쓰가 원하는대로 막 추가하고 수정하면 됨 ㅇㅇ
mbti_careers = {
    "ISTJ": ["회계사", "공무원", "경찰관", "프로그래머"],
    "ISFJ": ["간호사", "사회복지사", "교사", "사서"],
    ""
    "INFJ": ["상담사", "심리학자", "작가", "예술가"],
    "INTJ": ["과학자", "교수", "IT 개발자", "전략가"],
    "ISTP": ["엔지니어", "정비사", "소방관", "기술자"],
    "ISFP": ["디자이너", "음악가", "요리사", "수의사"],
    "INFP": ["시인", "작가", "미술 치료사", "대학교수"],
    "INTP": ["연구원", "철학자", "데이터 과학자", "발명가"],
    "ESTP": ["사업가", "영업직", "경찰", "스포츠 강사"],
    "ESFP": ["연예인", "유튜버", "어린이집 교사", "이벤트 플래너"],
    "ENFP": ["강사", "마케터", "연극인", "크리에이터"],
    "ENTP": ["창업가", "변호사", "엔지니어", "컨설턴트"],
    "ESTJ": ["관리자", "회계사", "기업가", "은행원"],
    "ESFJ": ["영업 관리", "인사 담당", "의사", "교사"],
    "ENFJ": ["사회 운동가", "정치인", "HR 전문가", "코치"],
    "ENTJ": ["사업가", "경영 컨설턴트", "변호사", "리더"]
}

st.set_page_config(page_title="MBTI 맞춤 진로 가이드 🚀", layout="centered")

st.title("나의 MBTI는 어떤 직업과 찰떡일까? ✨")
st.markdown("---")

# 현정쓰의 MBTI를 선택해주세요!
selected_mbti = st.selectbox(
    "본인의 MBTI를 선택해주세요:",
    ["선택하세요"] + list(mbti_careers.keys()), # "선택하세요"를 맨 앞에 넣어줌
    index=0 # 기본값으로 "선택하세요"가 보이도록
)

if selected_mbti != "선택하세요":
    st.subheader(f"✅ {selected_mbti}인 현정쓰에게 추천하는 직업은요...")

    # 해당 MBTI에 맞는 직업 추천
    careers = mbti_careers.get(selected_mbti, ["정보를 찾을 수 없어요 😅"])

    for career in careers:
        st.write(f"- {career}") # 리스트로 깔끔하게 보여줌
    
    st.markdown("---")
    st.info("이 추천은 참고용이에요! 중요한 건 현정쓰가 진짜 좋아하는 걸 찾는 거지! 😊")

else:
    st.warning("👆 위에서 현정쓰의 MBTI를 선택해주세요!")

st.markdown("""
<style>
.stSelectbox {
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

