import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título de la aplicación
st.title('Filtros de Regiones y Estados')

# Cargar el archivo Excel
url = 'https://github.com/icheano/DemoVentas/raw/main/SalidaFinal.xlsx'
df = pd.read_excel(url, sheet_name='Sheet1')

# Crear filtros de selección múltiple basados en las columnas 'Region' y 'State' y colocarlos en la barra lateral
region_seleccionada = st.sidebar.multiselect(
    'Selecciona una o más regiones',
    options=df['region'].unique(),
    default=df['region'].unique()
)

estado_seleccionado = st.sidebar.multiselect(
    'Selecciona uno o más estados',
    options=df['estado'].unique(),
    default=df['estado'].unique()
)

# Filtrar el DataFrame basado en la selección del usuario
df_filtrado = df[(df['region'].isin(region_seleccionada)) & (df['estado'].isin(estado_seleccionado))]

# Mostrar el DataFrame filtrado
st.write('DataFrame Filtrado:')
st.dataframe(df_filtrado)

# Crear una gráfica de pastel basada en la columna 'Category'
st.write('Gráfica de Pastel por Categoría:')
categoria_counts = df_filtrado['Category'].value_counts()

fig, ax = plt.subplots()
ax.pie(categoria_counts, labels=categoria_counts.index, autopct='%1.1f%%')
ax.axis('equal')  # Para asegurar que el pastel es un círculo.

st.pyplot(fig)
streamlit run streamlit_app.py
