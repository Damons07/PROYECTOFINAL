# pages/TendenciasTemporales.py
import streamlit as st
import plotly.express as px

def show(datos_filtrados):
    st.subheader("Tendencias Temporales")
    fig_tendencias_temporales = px.line(datos_filtrados, x='Fecha pedido', y='Importe venta total',
                                        title='Tendencias de Ventas a lo largo del Tiempo')
    st.plotly_chart(fig_tendencias_temporales)


