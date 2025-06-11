import pandas as pd

# 파일 불러오기
df = pd.read_csv("성취에_대한_만족도__19세_이상_인구__20250605123253.csv", encoding="utf-8-sig")

# 열 이름 확인
st.write("📋 열 목록 (Columns):")
st.write(df.columns.tolist())
