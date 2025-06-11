import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# CSV 불러오기
try:
    df = pd.read_csv("성취에_대한_만족도__19세_이상_인구__20250605123253.csv", encoding="utf-8-sig")
except UnicodeDecodeError:
    df = pd.read_csv("성취에_대한_만족도__19세_이상_인구__20250605123253.csv", encoding="cp949")

st.title("Satisfaction with Achievement - Visualization")

# 기준 선택 (성별, 연령별, 교육수준 등)
criteria_options = df["특성별(1)"].unique().tolist()
selected_criteria = st.selectbox("Select category", criteria_options)

# 선택된 기준으로 필터링
filtered_df = df[df["특성별(1)"] == selected_criteria]

# 만족도 항목
satisfaction_cols = ["2024.1", "2024.2", "2024.3", "2024.4", "2024.5"]
satisfaction_labels = ["Very satisfied", "Somewhat satisfied", "Neutral", "Somewhat dissatisfied", "Very dissatisfied"]

st.subheader(f"Satisfaction by {selected_criteria}")
for index, row in filtered_df.iterrows():
    st.markdown(f"### {row['특성별(2)']}")

    values = [row[col] for col in satisfaction_cols]

    fig, ax = plt.subplots()
    ax.bar(satisfaction_labels, values, color="cornflowerblue")
    ax.set_ylim(0, 100)
    ax.set_ylabel("Percentage (%)")
    ax.set_xlabel("Satisfaction Level")
    ax.set_title(f"{row['특성별(2)']} - Satisfaction")
    st.pyplot(fig)
