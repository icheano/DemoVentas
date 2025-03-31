import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título de la aplicación
st.title('Filtros de Region y State')

# Cargar el archivo Excel
url = 'https://github.com/icheano/DemoVentas/raw/main/SalidaFinal.xlsx'
df = pd.read_excel(url, sheet_name='Sheet1')

# Crear filtros de selección múltiple basados en las columnas 'Region' y 'State' y colocarlos en la barra lateral
region_seleccionada = st.sidebar.multiselect(
    'Selecciona una o más regiones',
    options=df['Region'].unique(),
    default=df['Region'].unique()
)

estado_seleccionado = st.sidebar.multiselect(
    'Selecciona uno o más estados',
    options=df['State'].unique(),
    default=df['State'].unique()
)

# Filtrar el DataFrame basado en la selección del usuario
df_filtrado = df[(df['Region'].isin(region_seleccionada)) & (df['State'].isin(estado_seleccionado))]

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




import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo Excel
url = 'https://github.com/icheano/DemoVentas/raw/main/SalidaFinal.xlsx'
df = pd.read_excel(url, sheet_name='Sheet1')

# Título de la aplicación
st.title('Ventas Acumuladas por Año, Categoría y Subcategoría (Barras) o Ventas Acumuladas por Región')

# Crear filtros de selección múltiple basados en las columnas 'region' y 'estado' y colocarlos en la barra lateral
region_seleccionada = st.sidebar.multiselect(
    'Selecciona una o más regiones',
    options=df['Region'].unique(),
    default=df['Region'].unique()
)

# Filtrar el DataFrame basado en la selección del usuario para 'Region'
df_filtrado_region = df[df['Region'].isin(Region_seleccionada)]

state_seleccionado = st.sidebar.multiselect(
    'Selecciona uno o más estados',
    options=df_filtrado_region['State'].unique(),
    default=df_filtrado_region['State'].unique()
)

# Filtrar el DataFrame basado en la selección del usuario para 'Region' y 'State'
df_filtrado = df[(df['Region'].isin(Region_seleccionada)) & (df['State'].isin(State_seleccionado))]

# Mostrar el DataFrame filtrado
st.write('DataFrame Filtrado:')
st.dataframe(df_filtrado)

# Crear una gráfica de pastel basada en la columna 'Category'
st.write('Gráfica de Pastel por Categoría:')
categoria_counts = df_filtrado['Category'].value_counts()

# Mostrar la gráfica de pastel
fig, ax = plt.subplots()
ax.pie(categoria_counts, labels=categoria_counts.index, autopct='%1.1f%%')
ax.axis('equal')  # Para asegurar que el pastel es un círculo.
st.pyplot(fig)

# Crear una gráfica de barras para ventas acumuladas por año, categoría y subcategoría
st.write('Ventas Acumuladas por Año, Categoría y Subcategoría (Barras):')
ventas_acumuladas = df_filtrado.groupby(['Year', 'Category', 'SubCategory'])['Sales'].sum().reset_index()

fig, ax = plt.subplots(figsize=(10, 6))
ventas_acumuladas.pivot(index='Year', columns=['Category', 'SubCategory'], values='Sales').plot(kind='bar', ax=ax)
plt.title('Ventas Acumuladas por Año, Categoría y Subcategoría')
plt.xlabel('Año')
plt.ylabel('Ventas Acumuladas')
plt.legend(title='Categoría y Subcategoría', bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig)

# Crear una gráfica de barras para ventas acumuladas por región
st.write('Ventas Acumuladas por Región:')
ventas_por_region = df_filtrado.groupby('region')['Sales'].sum().reset_index()

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(ventas_por_region['region'], ventas_por_region['Sales'])
plt.title('Ventas Acumuladas por Región')
plt.xlabel('Región')
plt.ylabel('Ventas Acumuladas')
st.pyplot(fig)

