import streamlit as st
import pandas as pd
import datetime 

#base de datos

walmart_link ='https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv'
walmart_data = pd.read_csv(walmart_link)

#Titulo

st.title("Activate 1 Caso Walmart")
st.subheader("Deberás construir la estructura  básica de una aplicación web que contenga una sección principal y además un apartado denominado barra lateral, el cual contendrá algunos controles para que se pueda manipular los datos sobre el proyecto de visualización de analítica de datos para WalMart USA.")

#se crea sidebar
sidebar = st.sidebar

#ponemos titulo y texto de sidebar
sidebar.title("Funciones laterales")

# Boton para desplegar base de datos
st.header("Dataset")
agree = sidebar.checkbox("Quieres ver la base de datos ? ")
if agree:
    st.dataframe(walmart_data)

#Filtros

menvio = sidebar.selectbox(
    "Modo de envio:",
    options = walmart_data["Ship Mode"].unique()
)

segmento = sidebar.selectbox(
    "Selecciona el segmento :",
    options = walmart_data["Segment"].unique()
)

pais = sidebar.selectbox(
    "Selecciona un país :",
    options = walmart_data["Country"].unique()
)

df1_selection = walmart_data[
    (walmart_data['Ship Mode'] == menvio) &
    (walmart_data['Segment'] == segmento) &
    (walmart_data['Country'] == pais) 
]

# el deploy del db del filtro


st.header("Dataset con filtros")
agree = sidebar.checkbox("Quieres ver la base de datos con filtros ? ")
if agree:
    st.dataframe(df1_selection)

import plotly.express as px

df = px.data.stocks()
fig = px.histogram(df, x="date")
fig.update_layout(bargap=0.2)
fig.show()
