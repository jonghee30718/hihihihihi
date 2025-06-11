import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import platform

# ✅ 한글 폰트 설정
import matplotlib
if platform.system() == 'Linux':
    matplotlib.rc('font', family='NanumGothic')
elif platform.system() == 'Windows':
    matplotlib.rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin':
    matplotlib.rc('font', family='AppleGothic')
matplotlib.rcParams['axes.unicode_minus'] = False

# ✅ CSV 읽기
try:
    df = pd.read_csv("성취에_대한_만족도__19세_이상_인구__20250605123253.csv", encoding="utf-8-sig")
except UnicodeDecodeError:
    df = pd.read_csv("성취에_대한_만족도__19세_이상_인구__20250605123253.csv", encoding="cp949")

st.title("성취에 대한 만족도 시각화")

# 기준 선택
criteria_options = df["특성별(1)"].unique().tolist()
selected_criteria = st.selectbox("기준을 선택하세요", criteria_options)

filtered_df = df[df["특성별(1)"] == selected_criteria]

# 만족도 항목
satisfaction_cols = ["2024.1", "2024.2", "2024.3", "2024.4", "2024.5"]
satisfaction_labels = ["매우 만족", "약간 만족", "보통", "약간 불만족", "매우 불만족"]

st.subheader(f"{selected_criteria}별 만족도")
for index, row in filtered_df.iterrows():
    st.markdown(f"### {row['특성별(2)']}")

    values = [row[col] for col in satisfaction_cols]

    fig, ax = plt.subplots()
    ax.bar(satisfaction_labels, values, color="skyblue")
    ax.set_ylim(0, 100)
    ax.set_ylabel("비율 (%)")
    ax.set_xlabel("만족도")
    ax.set_title(f"{row['특성별(2)']} - 만족도")
    st.pyplot(fig)
