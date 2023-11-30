# pages/ComparacionVariables.py
import streamlit as st
import plotly.express as px

def show(datos_filtrados):
    st.subheader("Comparación de Variables")
    fig_comparacion = px.scatter(datos_filtrados, x='Importe venta total', y='Importe Coste total',
                                 color='País', size='Unidades',
                                 title='Comparación de Ventas vs. Costos por País')
    st.plotly_chart(fig_comparacion)

