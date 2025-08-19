import streamlit as st
import pandas as pd

# 페이지 기본 설정
st.set_page_config(
    page_title="MBTI 시험 기간 멘탈 관리 가이드",
    page_icon="EMOJI_0",
    layout="wide"
)

# MBTI 유형별 데이터
mbti_data = {
    'ISTJ': {
        '특성': '체계적이고 책임감이 강함',
        '스트레스_요인': ['갑작스러운 계획 변경', '비효율적인 공부 환경', '불명확한 시험 범위'],
        '관리법': ['명확한 일정표 작성하기', '조용한 공부 환경 확보하기', '체크리스트로 진도 관리하기', '규칙적인 휴식 시간 갖기'],
        '추천_공부법': '개념을 체계적으로 정리하고 반복 학습하는 방식',
        '색상': '#1E88E5'  # 파란색
    },
    'ISFJ': {
        '특성': '세심하고 헌신적임',
        '스트레스_요인': ['과도한 경쟁 환경', '급격한 변화', '타인의 기대에 대한 부담'],
        '관리법': ['소규모 스터디 그룹 활용하기', '익숙한 환경에서 공부하기', '감정 일기 쓰기', '좋아하는 음악 들으며 휴식하기'],
        '추천_공부법': '노트 정리와 실생활 연관 지어 이해하기',
        '색상': '#7CB342'  # 녹색
    },
    'INFJ': {
        '특성': '이상주의적이고 통찰력이 뛰어남',
        '스트레스_요인': ['의미 없는 암기식 공부', '지나친 소음과 혼잡함', '가치관과 맞지 않는 과목'],
        '관리법': ['공부의 의미와 목적 되새기기', '명상과 심호흡으로 마음 다스리기', '창의적 시각화 기법 활용하기', '자연 속에서 휴식 취하기'],
        '추천_공부법': '개념 간 연결성을 찾고 큰 그림 이해하기',
        '색상': '#8E24AA'  # 보라색
    },
    'INTJ': {
        '특성': '전략적이고 독립적임',
        '스트레스_요인': ['비논리적인 학습 방식', '시간 낭비', '능력 발휘 못하는 상황'],
        '관리법': ['장기적 학습 전략 세우기', '독립적 공부 시간 확보하기', '지식 체계화하기', '새로운 지적 도전으로 기분 전환하기'],
        '추천_공부법': '개념을 분석하고 체계적으로 접근하기',
        '색상': '#3949AB'  # 남색
    },
    'ISTP': {
        '특성': '논리적이고 적응력이 뛰어남',
        '스트레스_요인': ['지나친 이론 중심 학습', '장기간 앉아있는 공부', '엄격한 규칙과 틀'],
        '관리법': ['실용적인 문제 해결에 집중하기', '짧은 집중 시간과 휴식 번갈아가며 공부하기', '손으로 무언가 만지작거리며 공부하기', '취미 활동으로 머리 식히기'],
        '추천_공부법': '실전 문제 풀이와 실습 중심 학습',
        '색상': '#EF6C00'  # 주황색
    },
    'ISFP': {
        '특성': '예술적이고 조화를 추구함',
        '스트레스_요인': ['경직된 학습 환경', '지나친 경쟁', '창의성 발휘 못하는 과목'],
        '관리법': ['아름다운 공부 환경 만들기', '시각적 학습 도구 활용하기', '예술 활동으로 스트레스 해소하기', '감각적 경험으로 기분 전환하기'],
        '추천_공부법': '시각화와 개인적 의미 부여하며 학습하기',
        '색상': '#D81B60'  # 분홍색
    },
    'INFP': {
        '특성': '이상주의적이고 창의적임',
        '스트레스_요인': ['경쟁적인 학습 환경', '기계적 암기', '자기표현 제한'],
        '관리법': ['자신만의 의미 있는 학습 목표 설정하기', '감정 일기 쓰기', '창작 활동으로 스트레스 해소하기', '조용한 사색 시간 갖기'],
        '추천_공부법': '자신과 연결된 의미를 찾아 학습하기',
        '색상': '#6A1B9A'  # 진한 보라색
    },
    'INTP': {
        '특성': '논리적이고 창의적임',
        '스트레스_요인': ['지나친 세부사항 암기', '반복적인 과제', '비논리적인 규칙'],
        '관리법': ['개념 간 연결성 탐구하기', '새로운 지식 탐험하기', '사고 실험하기', '독립적 사색 시간 확보하기'],
        '추천_공부법': '개념의 원리와 이론 탐구하기',
        '색상': '#0097A7'  # 청록색
    },
    'ESTP': {
        '특성': '활동적이고 현실적임',
        '스트레스_요인': ['장시간 앉아있는 공부', '추상적인 이론', '엄격한 규칙'],
        '관리법': ['활동적인 학습법 활용하기', '그룹 스터디로 에너지 얻기', '짧은 집중과 휴식 번갈아가며 공부하기', '운동으로 스트레스 해소하기'],
        '추천_공부법': '실전 문제 풀이와 체험 학습',
        '색상': '#FF5722'  # 밝은 주황색
    },
    'ESFP': {
        '특성': '즉흥적이고 사교적임',
        '스트레스_요인': ['혼자 공부하는 시간', '단조로운 학습 방식', '장기 계획'],
        '관리법': ['친구들과 함께 공부하기', '게임처럼 학습 만들기', '음악 들으며 공부하기', '소셜 활동으로 스트레스 해소하기'],
        '추천_공부법': '그룹 스터디와 대화식 학습',
        '색상': '#FF9800'  # 주황색
    },
    'ENFP': {
        '특성': '열정적이고 창의적임',
        '스트레스_요인': ['반복적인 암기', '엄격한 규칙', '자유로운 표현 제한'],
        '관리법': ['공부에 의미와 재미 찾기', '다양한 학습 방법 시도하기', '브레인스토밍으로 아이디어 정리하기', '창의적 취미로 기분 전환하기'],
        '추천_공부법': '연관성 찾기와 창의적 학습',
        '색상': '#E91E63'  # 핑크색
    },
    'ENTP': {
        '특성': '논쟁적이고 혁신적임',
        '스트레스_요인': ['지루한 암기 과목', '융통성 없는 규칙', '도전 부족'],
        '관리법': ['학습 내용에 대해 토론하기', '새로운 학습 방식 시도하기', '지식을 실생활에 적용해보기', '지적 도전으로 기분 전환하기'],
        '추천_공부법': '개념 비판과 토론식 학습',
        '색상': '#673AB7'  # 보라색
    },
    'ESTJ': {
        '특성': '체계적이고 결단력 있음',
        '스트레스_요인': ['비효율적인 학습 환경', '불명확한 지시사항', '계획 차질'],
        '관리법': ['명확한 목표와 일정 설정하기', '체계적인 학습 계획 세우기', '진도 체크하며 성취감 느끼기', '규칙적인 운동으로 스트레스 해소하기'],
        '추천_공부법': '체계적 정리와 실전 문제 풀이',
        '색상': '#2196F3'  # 파란색
    },
    'ESFJ': {
        '특성': '친절하고 배려심 깊음',
        '스트레스_요인': ['혼자서 결정해야 하는 상황', '갈등 상황', '타인의 부정적 반응'],
        '관리법': ['스터디 그룹 활용하기', '다른 사람 가르치며 공부하기', '정돈된 환경에서 공부하기', '친구들과 시간 보내며 휴식하기'],
        '추천_공부법': '협동 학습과 실용적 지식 습득',
        '색상': '#4CAF50'  # 녹색
    },
    'ENFJ': {
        '특성': '카리스마 있고 영감을 주는',
        '스트레스_요인': ['가치관과 맞지 않는 과목', '타인과의 불화', '피드백 부족'],
        '관리법': ['학습의 의미와 가치 찾기', '그룹 스터디 리드하기', '타인 돕는 시간 갖기', '사람들과 대화로 에너지 충전하기'],
        '추천_공부법': '토론과 가르치는 방식으로 학습',
        '색상': '#9C27B0'  # 보라색
    },
    'ENTJ': {
        '특성': '리더십 있고 전략적임',
        '스트레스_요인': ['비효율적인 시간 사용', '무능력한 환경', '통제력 상실'],
        '관리법': ['장기적 학습 전략 세우기', '목표 달성 계획 세우기', '효율적 시간 관리하기', '새로운 도전으로 스트레스 해소하기'],
        '추천_공부법': '전략적 학습 계획과 토론',
        '색상': '#283593'  # 짙은 남색
    }
}

# 메인 함수
def main():
    st.title("EMOJI_0 MBTI별 시험 기간 스트레스 & 멘탈 관리법")
    st.markdown("### 당신의 MBTI 유형에 맞는 최적의 시험 기간 관리법을 찾아보세요!")
    
    # 사이드바 - MBTI 선택
    st.sidebar.header("MBTI 선택")
    selected_mbti = st.sidebar.selectbox(
        "당신의 MBTI를 선택하세요",
        list(mbti_data.keys())
    )
    
    # 탭 생성
    tab1, tab2, tab3 = st.tabs(["EMOJI_1 MBTI 분석", "EMOJI_2‍♀️ 스트레스 관리법", "EMOJI_3 나만의 공부 계획"])
    
    # 탭 1: MBTI 분석
    with tab1:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.header(f"{selected_mbti} 특성")
            st.markdown(f"**주요 특성:** {mbti_data[selected_mbti]['특성']}")
            
            st.subheader("스트레스 요인")
            for factor in mbti_data[selected_mbti]['스트레스_요인']:
                st.markdown(f"- {factor}")
            
            st.subheader("추천 공부법")
            st.markdown(f"**{mbti_data[selected_mbti]['추천_공부법']}**")
        
        with col2:
            # MBTI 유형별 특성 점수 차트 (matplotlib 대신 streamlit 내장 차트 사용)
            st.subheader("MBTI 특성 분석")
            
            # 특성 점수 계산 (간단한 알고리즘)
            scores = {}
            
            # 내향형/외향형
            if selected_mbti[0] == 'I':
                scores['집중력'] = 80
                scores['사회성'] = 40
            else:  # 'E'
                scores['집중력'] = 60
                scores['사회성'] = 90

                        # 감각형/직관형
            if selected_mbti[1] == 'S':
                scores['체계성'] = 85
                scores['창의성'] = 50
            else:  # 'N'
                scores['체계성'] = 60
                scores['창의성'] = 90
                
            # 사고형/감정형
            if selected_mbti[2] == 'T':
                scores['분석력'] = 85
                scores['공감력'] = 50
            else:  # 'F'
                scores['분석력'] = 60
                scores['공감력'] = 85
                
            # 판단형/인식형
            if selected_mbti[3] == 'J':
                scores['계획성'] = 90
                scores['적응력'] = 55
            else:  # 'P'
                scores['계획성'] = 55
                scores['적응력'] = 85
            
            # 차트 데이터 생성
            chart_data = pd.DataFrame({
                '특성': list(scores.keys()),
                '점수': list(scores.values())
            })
            
            # 차트 표시
            st.bar_chart(chart_data.set_index('특성'))
            
            # 색상 표시
            st.markdown(f"<div style='background-color:{mbti_data[selected_mbti]['색상']}; height:20px; border-radius:5px;'></div>", unsafe_allow_html=True)
    
    # 탭 2: 스트레스 관리법
    with tab2:
        st.header(f"{selected_mbti}를 위한 시험 기간 멘탈 관리법")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            for i, tip in enumerate(mbti_data[selected_mbti]['관리법']):
                st.markdown(f"### Tip {i+1}: {tip}")
                st.markdown(get_tip_description(tip))
                st.markdown("---")
        
        with col2:
            st.subheader("멘탈 관리 팁")
            st.info("EMOJI_0 시험 전날에는 충분한 수면을 취하세요.")
            st.info("EMOJI_1 적절한 휴식과 공부의 균형을 유지하세요.")
            st.info("EMOJI_2 부정적 생각이 들면 잠시 멈추고 심호흡하세요.")
    
    # 탭 3: 나만의 공부 계획
    with tab3:
        st.header("EMOJI_3 나만의 맞춤 공부 계획 만들기")
        
        st.write(f"{selected_mbti} 유형에 맞는 공부 계획을 세워봅시다!")
        
        # 사용자 입력 받기
        col1, col2 = st.columns(2)
        
        with col1:
            subject = st.text_input("과목명", "")
            start_date = st.date_input("시작일")
            end_date = st.date_input("종료일")
        
        with col2:
            daily_hours = st.slider("하루 공부 시간 (시간)", 1, 12, 4)
            difficulty = st.select_slider("난이도", options=["쉬움", "보통", "어려움", "매우 어려움"])
        
        if st.button("공부 계획 생성"):
            if subject:
                create_study_plan(selected_mbti, subject, start_date, end_date, daily_hours, difficulty)
            else:
                st.error("과목명을 입력해주세요.")

# 팁 설명 함수
def get_tip_description(tip):
    # 팁별 상세 설명
    descriptions = {
        "명확한 일정표 작성하기": "시험 범위를 세분화하고 각 과목별 공부 시간을 할당하세요. 체크리스트를 만들어 진행 상황을 확인하며 성취감을 느껴보세요.",
        "조용한 공부 환경 확보하기": "방해 요소가 없는 조용한 공간에서 집중력을 극대화하세요. 필요하다면 소음 차단 이어폰을 활용해보세요.",
        "체크리스트로 진도 관리하기": "공부할 내용을 작은 단위로 나누고, 완료할 때마다 체크하며 성취감을 느껴보세요.",
        "규칙적인 휴식 시간 갖기": "25분 공부 후 5분 휴식하는 뽀모도로 기법을 활용해 효율적으로 공부해보세요."
    }
    
    # 기본 설명
    default = "이 방법은 당신의 MBTI 특성에 맞게 스트레스를 효과적으로 관리하는 데 도움이 됩니다."
    
    return descriptions.get(tip, default)

# 공부 계획 생성 함수
def create_study_plan(mbti, subject, start_date, end_date, daily_hours, difficulty):
    # 계획 생성 로직
    days = (end_date - start_date).days + 1
    
    st.success(f"✅ {subject} 과목 {days}일 공부 계획이 생성되었습니다!")
    
    # MBTI별 맞춤 조언
    st.subheader("EMOJI_4 MBTI 맞춤 학습 조언")
    st.markdown(f"**{mbti}** 유형은 **{mbti_data[mbti]['특성']}** 특성을 가지고 있어요.")
    st.markdown(f"**추천 공부법:** {mbti_data[mbti]['추천_공부법']}")
    
    # 일일 계획표 예시
    st.subheader("EMOJI_5 일일 계획표 예시")
    
    daily_plan = pd.DataFrame({
        "시간": [f"{i}:00 - {i+1}:00" for i in range(9, 9+daily_hours)],
        "활동": [f"{subject} 학습 - {i+1}단계" for i in range(daily_hours)]
    })
    
    st.table(daily_plan)
    
    # 진도율 표시
    st.subheader("EMOJI_6 예상 진도율")
    progress_data = pd.DataFrame({
        '일차': list(range(1, days+1)),
        '진도율': [min(100, i * (100/days) * 1.1) for i in range(1, days+1)]
    })
    st.line_chart(progress_data.set_index('일차'))
    
    # 다운로드 버튼
    st.download_button(
        label="EMOJI_7 공부 계획 다운로드",
        data=daily_plan.to_csv().encode('utf-8'),
        file_name=f'{subject}_study_plan.csv',
        mime='text/csv',
    )

# 메인 함수 실행
if __name__ == "__main__":
    main()
