#archivo_excel = "datos/registrosventas.xlsx"
import streamlit as st
import pandas as pd
import plotly.express as px
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns



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




#-----------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------

archivo_geojson = "datos/custom.geo.json"

try:
    gdf = gpd.read_file(archivo_geojson, driver='GeoJSON')
    print(gdf.head())
except Exception as e:
    print(f"Error al leer el archivo GeoJSON: {e}")


import geopandas as gpd

# Ruta al archivo GeoJSON
ruta_archivo = 'ruta/a/tu/archivo.geojson'

# Lee el archivo GeoJSON con geopandas
datos_geojson = gpd.read_file(ruta_archivo)

# Muestra los primeros registros del DataFrame geoespacial
print(datos_geojson.head())