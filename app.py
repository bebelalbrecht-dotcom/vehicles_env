import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Dashboard de Anúncios de Carros 🚗')

car_data = pd.read_csv('vehicles.csv')  # arquivo na raiz do projeto

if st.checkbox('Mostrar estatísticas descritivas'):
    st.write(car_data.describe())
    
if st.button('Criar histograma'):
    st.write('Histograma da quilometragem')
    fig_hist = px.histogram(car_data, x='odometer', nbins=50)
    st.plotly_chart(fig_hist, use_container_width=True)
    
