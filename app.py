import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Análisis de vehículos en venta - App Interactiva')

# Casilla de verificación para histograma
build_histogram = st.checkbox('Mostrar histograma del odómetro')

if build_histogram:
    st.write('Creación de un histograma para la columna "odometer"')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación para gráfico de dispersión
build_scatter = st.checkbox('Mostrar gráfico de dispersión (precio vs año)')

if build_scatter:
    st.write('Creación de un gráfico de dispersión entre "price" y "model_year"')
    fig2 = px.scatter(car_data, x="model_year", y="price")
    st.plotly_chart(fig2, use_container_width=True)
