import streamlit as st
import pandas as pd

st.write("""

Mi primera app
Hello World

""")
df = pd.read_csv("dataset.csv")
st.line_chart(df)
