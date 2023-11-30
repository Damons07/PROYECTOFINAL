# pages/ResumenProductos.py
import streamlit as st
import plotly.express as px

def show(datos_filtrados):
    st.subheader("Productos Más Vendidos")
    productos_mas_vendidos = datos_filtrados.groupby('Tipo de producto')['Unidades'].sum().reset_index()
    fig_productos_mas_vendidos = px.bar(productos_mas_vendidos, x='Tipo de producto', y='Unidades',
                                        title='Productos Más Vendidos', labels={'Unidades': 'Cantidad Vendida'})
    st.plotly_chart(fig_productos_mas_vendidos)
    show(datos_filtrados)