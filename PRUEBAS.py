# Importar librerías
import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
archivo_excel = "datos/registrosventas.xlsx"
datos_ventas = pd.read_excel(archivo_excel)

datos_ventas['Fecha pedido'] = pd.to_datetime(datos_ventas['Fecha pedido'])

# Título
st.title("Bienvenido, este es el Dashboard del Análisis de Ventas")

# Páginas dispoibles
paginas = ["Resumen Ejecutivo", "Distribución de Ventas", "Tendencias Temporales", "Mapa de Ventas", "Comparación de Variables", "Productos Más Vendidos"]

# Seleccionar la página
pagina_seleccionada = st.sidebar.selectbox("Selecciona una página", paginas)

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

# menuuuuu
if pagina_seleccionada == "Resumen Ejecutivo":
    st.subheader("Resumen Ejecutivo")
    total_ingresos = datos_filtrados['Importe venta total'].sum()
    total_costos = datos_filtrados['Importe Coste total'].sum()
    margen_beneficio_promedio = ((total_ingresos - total_costos) / total_ingresos) * 100
    st.metric("Ingresos Totales", f"${total_ingresos:,.2f}")
    st.metric("Costos Totales", f"${total_costos:,.2f}")
    st.metric("Margen de Beneficio Promedio", f"{margen_beneficio_promedio:.2f}%")

elif pagina_seleccionada == "Distribución de Ventas":
    st.subheader("Distribución de Ventas")
    fig_ventas_por_pais = px.bar(datos_filtrados, x='País', y='Importe venta total',
                                 title='Ventas por País', labels={'Importe venta total': 'Ventas'})
    st.plotly_chart(fig_ventas_por_pais)

elif pagina_seleccionada == "Tendencias Temporales":
    st.subheader("Tendencias Temporales")
    fig_tendencias_temporales = px.line(datos_filtrados, x='Fecha pedido', y='Importe venta total',
                                        title='Tendencias de Ventas a lo largo del Tiempo')
    st.plotly_chart(fig_tendencias_temporales)

elif pagina_seleccionada == "Mapa de Ventas":
    st.subheader("Mapa de Ventas")
    fig_mapa_ventas = px.scatter_geo(datos_filtrados, locations='País', color='Importe venta total',
                                     hover_name='País', size='Importe venta total',
                                     projection='natural earth', title='Mapa de Ventas')
    st.plotly_chart(fig_mapa_ventas)

elif pagina_seleccionada == "Comparación de Variables":
    st.subheader("Comparación de Variables")
    fig_comparacion = px.scatter(datos_filtrados, x='Importe venta total', y='Importe Coste total',
                                 color='País', size='Unidades',
                                 title='Comparación de Ventas vs. Costos por País')
    st.plotly_chart(fig_comparacion)

elif pagina_seleccionada == "Productos Más Vendidos":
    st.subheader("Productos Más Vendidos")
    productos_mas_vendidos = datos_filtrados.groupby('Tipo de producto')['Unidades'].sum().reset_index()
    fig_productos_mas_vendidos = px.bar(productos_mas_vendidos, x='Tipo de producto', y='Unidades',
                                        title='Productos Más Vendidos', labels={'Unidades': 'Cantidad Vendida'})
    st.plotly_chart(fig_productos_mas_vendidos)
