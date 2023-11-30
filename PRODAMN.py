#archivo_excel = "datos/registrosventas.xlsx"
import streamlit as st
import pandas as pd
import plotly.express as px
import geopandas as gpd


# Cargar los datos
archivo_excel = "datos/registrosventas.xlsx"
datos_ventas = pd.read_excel(archivo_excel)

datos_ventas['Fecha pedido'] = pd.to_datetime(datos_ventas['Fecha pedido'])

# Título
st.title("Bienvenido, este es el Dashboard del Análisis de Ventas")


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

# Filtrar datos según las fechas seleccionadas
datos_filtrados = datos_ventas[(datos_ventas['Fecha pedido'] >= pd.to_datetime(fecha_inicio)) &
                               (datos_ventas['Fecha pedido'] <= pd.to_datetime(fecha_fin))]


# Resumen Ejecutivo
st.subheader("Resumen Ejecutivo")
total_ingresos = datos_filtrados['Importe venta total'].sum()
total_costos = datos_filtrados['Importe Coste total'].sum()
margen_beneficio_promedio = ((total_ingresos - total_costos) / total_ingresos) * 100
Utilidad = total_ingresos - total_costos

st.metric("Ingresos Totales", f"${total_ingresos:,.2f}")
st.metric("Costos Totales", f"${total_costos:,.2f}")
st.metric("Margen de Beneficio Promedio", f"{margen_beneficio_promedio:.2f}%")
st.metric("Utilidad", f"${Utilidad:,.2f}")

# Gráficos de Distribución
#1
st.subheader("Distribución de Ventas")
fig_ventas_por_pais = px.bar(datos_filtrados, x='País', y='Importe venta total',
                             title='Ventas por País', labels={'Importe venta total': 'Ventas'})
st.plotly_chart(fig_ventas_por_pais)

#2
fig_ventas_por_producto = px.bar(datos_filtrados, x='Tipo de producto', y='Importe venta total',
                                 title='Ventas por Tipo de Producto', labels={'Importe venta total': 'Ventas'})
st.plotly_chart(fig_ventas_por_producto)

# Tendencias Temporales
st.subheader("Tendencias Temporales")
fig_tendencias_temporales = px.line(datos_filtrados, x='Fecha pedido', y='Importe venta total',
                                    title='Tendencias de Ventas a lo largo del Tiempo')
st.plotly_chart(fig_tendencias_temporales)

# Mapaaaa
st.subheader("Mapa de Ventas")
fig_mapa_ventas = px.scatter_geo(datos_filtrados, locations='País', color='Importe venta total',
                                 hover_name='País', size='Importe venta total',
                                 projection='natural earth', title='Mapa de Ventas')
st.plotly_chart(fig_mapa_ventas)


# Comparación de Variables
st.subheader("Comparación de Variables")
fig_comparacion = px.scatter(datos_filtrados, x='Importe venta total', y='Importe Coste total',
                             color='País', size='Unidades',
                             title='Comparación de Ventas vs. Costos por País')
st.plotly_chart(fig_comparacion)

# Resumen de Productos
st.subheader("Productos Más Vendidos")
productos_mas_vendidos = datos_filtrados.groupby('Tipo de producto')['Unidades'].sum().reset_index()
fig_productos_mas_vendidos = px.bar(productos_mas_vendidos, x='Tipo de producto', y='Unidades',
                                    title='Productos Más Vendidos', labels={'Unidades': 'Cantidad Vendida'})
st.plotly_chart(fig_productos_mas_vendidos)