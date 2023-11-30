# pages/ResumenEjecutivo.py
import streamlit as st
import pandas as pd

def show(datos_filtrados):
    st.subheader("Resumen Ejecutivo")
    total_ingresos = datos_filtrados['Importe venta total'].sum()
    total_costos = datos_filtrados['Importe Coste total'].sum()
    margen_beneficio_promedio = ((total_ingresos - total_costos) / total_ingresos) * 100
    Utilidad = total_ingresos - total_costos

    st.metric("Ingresos Totales", f"${total_ingresos:,.2f}")
    st.metric("Costos Totales", f"${total_costos:,.2f}")
    st.metric("Margen de Beneficio Promedio", f"{margen_beneficio_promedio:.2f}%")
    st.metric("Utilidad", f"${Utilidad:,.2f}")
