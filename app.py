import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Dashboard de Anúncios de Carros 🚗')

car_data = pd.read_csv('vehicles.csv')  # arquivo na raiz do projeto