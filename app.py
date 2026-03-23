import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Dashboard de Anúncios de Carros 🚗')

car_data = pd.read_csv('vehicles.csv')  # arquivo na raiz do projeto

if st.checkbox('Mostrar estatísticas descritivas'):
    st.write(car_data.describe())
st.subheader('Filtros')

max_odometer = st.slider(
    'Quilometragem máxima',
    0,
    int(car_data['odometer'].max()),
    100000
)

max_price = st.slider(
    'Preço máximo',
    0,
    int(car_data['price'].max()),
    20000
)

filtered_data = car_data[
    (car_data['odometer'] <= max_odometer) &
    (car_data['price'] <= max_price)
]

if st.button('Criar histograma'):
    st.write('Histograma da quilometragem')
    fig_hist = px.histogram(filtered_data, x='odometer', nbins=50)
    st.plotly_chart(fig_hist, use_container_width=True)

# 🔹 BOTÃO DISPERSÃO
if st.button('Criar gráfico de dispersão'):
    st.write('Preço vs Quilometragem')
    fig_scatter = px.scatter(filtered_data, x='odometer', y='price')
    st.plotly_chart(fig_scatter, use_container_width=True)
