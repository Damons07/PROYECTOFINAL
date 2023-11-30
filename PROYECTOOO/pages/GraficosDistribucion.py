# pages/GraficosDistribucion.py
import streamlit as st
import plotly.express as px

def show(datos_filtrados):
    st.subheader("Distribución de Ventas")
    fig_ventas_por_pais = px.bar(datos_filtrados, x='País', y='Importe venta total',
                                 title='Ventas por País', labels={'Importe venta total': 'Ventas'})
    st.plotly_chart(fig_ventas_por_pais)
