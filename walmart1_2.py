import streamlit as st
import pandas as pd
import datetime 
import plotly.express as px

#base de datos

walmart_link ='https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv'
walmart_data = pd.read_csv(walmart_link)

#Titulo

st.title("Activate 2 Caso Walmart")
st.subheader("Desarrollar un código sobre la estructura de una aplicación web que contenga 3 gráficas (barras, pastel y un histograma) sobre el proyecto de visualización de analítica de datos para WalMart USA.")


st.subheader("Histograma")
fig = px.histogram(walmart_data, x="State")
fig.update_layout(bargap=0.2)
st.write(fig)

st.subheader("Grafica de barras")
fig2 = px.bar(walmart_data, x="State", y="Sales", color="Segment", title="Grafica de barras")
st.write(fig2)
