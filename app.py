import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 파일 불러오기
try:
    df = pd.read_csv("성취에_대한_만족도__19세_이상_인구__20250605123253.csv", encoding="utf-8-sig")
except:
    df = pd.read_csv("성취에_대한_만족도__19세_이상_인구__20250605123253.csv", encoding="cp949")

st.title("Satisfaction with Achievement")

# 기준 선택
criteria_options = df["특성별(1)"].dropna().unique().tolist()
selected_criteria = st.selectbox("Select category", criteria_options)

# 만족도 관련 컬럼
satisfaction_cols = [
    "성취에 대한 만족도 - 매우 그렇다 (%)",
    "성취에 대한 만족도 - 대체로 그렇다 (%)",
    "성취에 대한 만족도 - 보통 (%)",
    "성취에 대한 만족도 - 별로 아니다 (%)",
    "성취에 대한 만족도 - 전혀 아니다 (%)",
]
satisfaction_labels = ["Very satisfied", "Somewhat satisfied", "Neutral", "Somewhat dissatisfied", "Very dissatisfied"]

# 선택된 기준에 해당하는 행 필터링
filtered_df = df[df["특성별(1)"] == selected_criteria]

# 그래프 출력
st.subheader(f"Satisfaction by {selected_criteria}")
for index, row in filtered_df.iterrows():
    st.markdown(f"### {row['특성별(2)']}")

    try:
        values = [float(row[col]) for col in satisfaction_cols if pd.notna(row[col])]
    except ValueError:
        st.write("Invalid data found. Skipping...")
        continue

    if not values or len(values) < 5:
        st.write("No data available for this category.")
        continue

    fig, ax = plt.subplots(figsize=(6, 3))
    ax.bar(satisfaction_labels, values, color="cornflowerblue")

    ax.set_ylim(0, max(values) + 10)
    ax.set_ylabel("Percentage (%)", fontsize=9)
    ax.set_xlabel("Satisfaction Level", fontsize=9)
    ax.set_title(f"{row['특성별(2)']} - Satisfaction", fontsize=10)
    ax.tick_params(axis='x', labelrotation=30, labelsize=8)
    ax.tick_params(axis='y', labelsize=8)

    st.pyplot(fig)
