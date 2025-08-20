import streamlit as st
import pandas as pd

# 페이지 기본 설정
st.set_page_config(
    page_title="✨내 MBTI 맞춤 시험 멘탈 케어✨",
    page_icon="🧠🎉",
    layout="wide"
)

# MBTI 유형별 데이터 (원본 유지)
# ...

def main():
    st.title("🧠 내 MBTI 별 시험 스트레스 탈출 가이드! 🚀")
    st.markdown("### 🤔 시험 스트레스? 내 MBTI가 답! 지금 바로 확인해봐요~")

    st.sidebar.header("🕵️‍♀️ MBTI 찾기")
    selected_mbti = st.sidebar.selectbox(
        "너의 MBTI를 골라줘봐 ↓",
        list(mbti_data.keys())
    )
    
    tab1, tab2, tab3 = st.tabs([ "🔍 MBTI 속속들이", "💆‍♀️ 스트레스 탈출법", "📝 나만의 스터디 플랜" ])
    
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.header(f"🎯 {selected_mbti} 캐릭터 분석!")
            st.markdown(f"**핵심 특성:** {mbti_data[selected_mbti]['특성']}")
            st.subheader("😵‍💫 스트레스 유발 요인")
            for factor in mbti_data[selected_mbti]['스트레스_요인']:
                st.markdown(f"– {factor}")
            st.subheader("📚 너를 위한 공부법 추천!")
            st.markdown(f"💡 {mbti_data[selected_mbti]['추천_공부법']}")
        with col2:
            scores = {}
            scores['집중력'] = 80 if selected_mbti[0] == 'I' else 60
            scores['사회성'] = 40 if selected_mbti[0] == 'I' else 90
            scores['체계성'] = 85 if selected_mbti[1] == 'S' else 60
            scores['창의성'] = 50 if selected_mbti[1] == 'S' else 90
            scores['분석력'] = 85 if selected_mbti[2] == 'T' else 60
            scores['공감력'] = 50 if selected_mbti[2] == 'T' else 85
            scores['계획성'] = 90 if selected_mbti[3] == 'J' else 55
            scores['적응력'] = 55 if selected_mbti[3] == 'J' else 85
            
            df = pd.DataFrame(list(scores.items()), columns=['능력', '점수'])
            st.subheader("📊 MBTI 나의 능력치!")
            st.bar_chart(df.set_index('능력'))

            st.markdown(
                f"<div style='background-color:{mbti_data[selected_mbti]['색상']}; height:25px; border-radius:10px; margin-top:10px;'>"
                f"</div>", unsafe_allow_html=True
            )

    with tab2:
        st.header(f"💪 {selected_mbti}의 시험 스트레스 싹~ 날려 버리는 비법!")
        col1, col2 = st.columns([3, 1])
        with col1:
            for i, tip in enumerate(mbti_data[selected_mbti]['관리법']):
                st.markdown(f"🌟 팁 {i+1}: **{tip}**")
                st.markdown(get_tip_description(tip))
                st.markdown("---")
        with col2:
            st.subheader("✨ 꿀팁 모음✨")
            st.info("🛌 시험 전날엔 무조건 꿀잠 자자!")
            st.info("☕ 가끔은 커피 대신 명상하기 추천~")
            st.info("😌 스트레스가 오면 좋아하는 노래 틀기!")

    with tab3:
        st.header("✍️ 나만의 똑똑한 공부 계획표 만들기")
        st.write(f"아이디어 폭발! {selected_mbti}에게 딱 맞는 스케줄링 시작~")
        col1, col2 = st.columns(2)

        with col1:
            subject = st.text_input("어떤 과목 집중할 거야?")
            start_date = st.date_input("공부 시작일")
            end_date = st.date_input("공부 끝날 날짜")

        with col2:
            daily_hours = st.slider("하루 공부 시간(시간)", 1, 12, 4)
            difficulty = st.select_slider("난이도 선택하기", options=["쉬움", "보통", "어려움", "아주 어려움"])

        if st.button("🚀 공부 계획 만들기!"):
            if subject:
                create_study_plan(selected_mbti, subject, start_date, end_date, daily_hours, difficulty)
            else:
                st.error("⚠️ 과목명을 꼭 입력해 주세요!")

def get_tip_description(tip):
    descriptions = {
        "명확한 일정표 작성하기": "시험 범위를 쪼개서 구체적으로 계획 세우면 공부할 맛이 난다구요!",
        "조용한 공부 환경 확보하기": "핸드폰 OFF, 집중력을 올려줄 완전 조용한 공간 찾아라!",
        "체크리스트로 진도 관리하기": "하루하루 체크하며 작지만 큰 성취감을 즐기자!",
        "규칙적인 휴식 시간 갖기": "25분 공부 후 5분 딱 쉬고, 반복학습의 힘을 키워봐요!"
    }
    return descriptions.get(tip, "당신에게 딱 맞는 최고의 스트레스 탈출법입니다!")

# 이하 create_study_plan 함수 등은 원래 코드 유지
# ...

if __name__ == "__main__":
    main()
