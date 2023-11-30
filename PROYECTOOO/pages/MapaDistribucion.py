# pages/MapaDistribucion.py
import streamlit as st
import plotly.express as px

def show(datos_filtrados):
    st.subheader("Mapa de Ventas")
    fig_mapa_ventas = px.scatter_geo(datos_filtrados, locations='País', color='Importe venta total',
                                     hover_name='País', size='Importe venta total',
                                     projection='natural earth', title='Mapa de Ventas')
    st.plotly_chart(fig_mapa_ventas)
