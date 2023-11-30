# Home.py
import streamlit as st
from pages import ResumenEjecutivo, GraficosDistribucion, TendenciasTemporales, MapaDistribucion, ComparacionVariables, ResumenProductos
import pandas as pd

# Cargar los datos
archivo_excel = "datos2/registrosventas.xlsx"
datos_ventas = pd.read_excel(archivo_excel)

# Filtrar datos según las fechas seleccionadas
fecha_minima = datos_ventas['Fecha pedido'].min().date()
fecha_maxima = datos_ventas['Fecha pedido'].max().date()
fecha_inicio = st.sidebar.date_input("Selecciona la fecha de inicio:",
                                     min_value=fecha_minima,
                                     max_value=fecha_maxima,
                                     value=fecha_minima)
fecha_fin = st.sidebar.date_input("Selecciona la fecha de fin:",
                                   min_value=fecha_inicio,
                                   max_value=fecha_maxima,
                                   value=fecha_maxima)
datos_filtrados = datos_ventas[(datos_ventas['Fecha pedido'] >= pd.to_datetime(fecha_inicio)) &
                               (datos_ventas['Fecha pedido'] <= pd.to_datetime(fecha_fin))]

def main():
    st.title("Streamlit Multi-Page App")

    # Menú de navegación en la página de inicio
    page = st.sidebar.selectbox("Selecciona una página",
                                ["Resumen Ejecutivo", "Gráficos de Distribución", "Tendencias Temporales",
                                 "Mapa de Distribución", "Comparación de Variables", "Resumen de Productos"])

    # Filtrar datos según las fechas seleccionadas
    datos_ventas_filtrados = datos_ventas[(datos_ventas['Fecha pedido'] >= pd.to_datetime(fecha_inicio)) &
                                          (datos_ventas['Fecha pedido'] <= pd.to_datetime(fecha_fin))]

    # Mostrar la página correspondiente según la selección
    if page == "Resumen Ejecutivo":
        ResumenEjecutivo.show(datos_ventas_filtrados)
    elif page == "Gráficos de Distribución":
        GraficosDistribucion.show(datos_ventas_filtrados)
    elif page == "Tendencias Temporales":
        TendenciasTemporales.show(datos_ventas_filtrados)
    elif page == "Mapa de Distribución":
        MapaDistribucion.show(datos_ventas_filtrados)
    elif page == "Comparación de Variables":
        ComparacionVariables.show(datos_ventas_filtrados)
    elif page == "Resumen de Productos":
        ResumenProductos.show(datos_ventas_filtrados)

if __name__ == "__main__":
    main()
