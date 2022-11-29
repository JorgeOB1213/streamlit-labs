import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

#base de datos

walmart_link ='https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv'
data = pd.read_csv(walmart_link)

#Titulo

st.title("Activate 2 Caso Walmart A01702048")
st.subheader("Desarrollar un código sobre la estructura de una aplicación web que contenga 3 gráficas (barras, pastel y un histograma) sobre el proyecto de visualización de analítica de datos para WalMart USA.")



sidebar = st.sidebar

Category = data['Category'].unique().tolist()
categ = sidebar.selectbox('¿Que Categoria quieres ver?', Category,0)
data = data[data['Category']==categ]

selected_class = sidebar.radio("Selecciona una clase",data['Ship Mode'].unique())
sidebar.write("Selected Class:", selected_class)
data = data[data['Ship Mode']==selected_class]

optionals = st.expander("Descuento", True)
fare_select = optionals.slider(
"Select the Fare",
min_value=float(data['Discount'].min()),
max_value=float(data['Discount'].max())
)

data = data[(data['Discount'] >= fare_select)]



agree = sidebar.checkbox("show DataSet Overview ? ")
if agree:

    st.dataframe(data)



st.header("Grafica de Barras de Walmart")

fig1 = px.bar(data, x='Ship Mode', y='Sales',title='Ventas por clase')
fig1.update_layout(
    xaxis = dict(
        tickmode = 'linear',
        tick0 = 0,
        dtick = 1
    )
)

st.plotly_chart(fig1)



df_p = data.groupby(['Region']).size().reset_index()
df_p.columns = ['Region' ,'Counts']
df_p['percentage'] = df_p.groupby(['Counts']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
df_p.columns = ['Region' ,'Counts', 'Percentage']
df_p['Percentage'] = (df_p['Counts'] / df_p['Counts'].sum()) * 100


fig = px.pie(df_p, values='Percentage', names='Region', title='Ventas por región de WaltMart USA')
st.plotly_chart(fig)


fig3 = px.histogram(data, x="Discount")
st.plotly_chart(fig3)

@st.cache
def load_data(nrows):
    DATA_URL = 'https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv'
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data['Order Date'] = pd.to_datetime(data['Order Date'])
    return data

data = load_data(100)

st.dataframe(data)
