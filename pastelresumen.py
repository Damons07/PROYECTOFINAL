import streamlit as st
import pandas as pd
import plotly.express as px
import geopandas as gpd


# Cargar los datos
archivo_excel = "datos/registrosventas.xlsx"
datos_ventas = pd.read_excel(archivo_excel)

datos_ventas['Fecha pedido'] = pd.to_datetime(datos_ventas['Fecha pedido'])

# Título
st.title("Productos más venidos")


fecha_minima = datos_ventas['Fecha pedido'].min().date()
fecha_maxima = datos_ventas['Fecha pedido'].max().date()

# Sidebar para opciones de análisis
st.sidebar.header("Configuración")
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

# Productos Más Vendidos
productos_mas_vendidos = datos_filtrados.groupby('Tipo de producto')['Unidades'].sum().reset_index()
fig_pie_productos_mas_vendidos = px.pie(productos_mas_vendidos, values='Unidades', names='Tipo de producto',
                                        title='Productos Más Vendidos', labels={'Unidades': 'Cantidad Vendida'})
st.plotly_chart(fig_pie_productos_mas_vendidos)
