import pandas as pd
import streamlit as st
import plotly.express as px

# Lee el archivo Excel
try:
  df = pd.read_excel('SalidaFinal.xlsx')
  print(df.head())  # Muestra las primeras filas del DataFrame
except FileNotFoundError:
  print("Error: El archivo 'SalidaFinal.xlsx' no se encuentra.")
except Exception as e:
  print(f"Error al leer el archivo: {e}")



# Lee el archivo Excel
try:
    # Agrupa por región y suma las ventas
    sales_by_region = df.groupby('Region')['Sales'].sum()

    # Crea la gráfica de barras con Plotly Express
    fig = px.bar(sales_by_region, 
                 x=sales_by_region.index, 
                 y='Sales', 
                 title='Ventas Acumuladas por Región',
                 labels={'Sales': 'Ventas', 'x': 'Región'})
    
    st.plotly_chart(fig)

except FileNotFoundError:
    st.error("Error: El archivo 'SalidaFinal.xlsx' no se encuentra.")
except Exception as e:
    st.error(f"Error al leer el archivo o generar la gráfica: {e}")
with st.sidebar:
# Aplica los filtros
# Filtro para la columna "Region"
  region_filter = st.selectbox("Selecciona una región:", df['Region'].unique())
  df_filtered = df[df['Region'] == region_filter]

# Segundo filtro para la columna "State" basado en el filtro de "Region"
  state_filter = st.selectbox("Selecciona un estado:", df_filtered['State'].unique())
  df_filtered = df_filtered[df_filtered['State'] == state_filter]




# Muestra el DataFrame filtrado
st.dataframe(df_filtered)

# Gráfica de pastel para la columna "Category"
category_counts = df_filtered['Category'].value_counts()
fig_pie = px.pie(category_counts, 
                     values=category_counts.values, 
                     names=category_counts.index, 
                     title='Distribución de Categorías')
st.plotly_chart(fig_pie)



# prompt: usando de dataframe df, crear 2 filtros con streamlit en un sidebar, uno con la columna Region y otro con la columna State e imprimir un solo resultado 

# Sidebar with filters
st.sidebar.header("Filtros")

# Region filter
selected_regions = st.sidebar.multiselect("Selecciona regiones", df['Region'].unique())

# State filter
selected_states = st.sidebar.multiselect("Selecciona estados", df['State'].unique())

# Apply filters
if selected_regions and selected_states:
    df_filtered = df[(df['Region'].isin(selected_regions)) & (df['State'].isin(selected_states))]
elif selected_regions:
    df_filtered = df[df['Region'].isin(selected_regions)]
elif selected_states:
    df_filtered = df[df['State'].isin(selected_states)]
else:
    df_filtered = df

# Display the filtered result (first row if available)
if not df_filtered.empty:
    st.write("Resultado del filtro:")
    st.dataframe(df_filtered.head(1))  # Show only the first row
else:
    st.write("No se encontraron resultados para los filtros seleccionados.")



# prompt: usando de dataframe df, crear 2 filtros con streamlit en un sidebar, uno con la columna Region y otro con la columna State e imprimir el dataframe. Tambien crea una grafica de pastel con la columna Category

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataframe
try:
    df = pd.read_excel('SalidaFinal.xlsx')
except FileNotFoundError:
    st.error("Error: Archivo 'SalidaFinal.xlsx' no encontrado. Verifica la ruta.")
    st.stop()
except Exception as e:
    st.error(f"Ocurrió un error al leer el archivo: {e}")
    st.stop()

# Sidebar with filters
st.sidebar.header("Filtros")

# Region filter
selected_regions = st.sidebar.multiselect("Selecciona regiones", df['Region'].unique())

# State filter
selected_states = st.sidebar.multiselect("Selecciona estados", df['State'].unique())

# Apply filters
if selected_regions:
    df = df[df['Region'].isin(selected_regions)]
if selected_states:
    df = df[df['State'].isin(selected_states)]


# Display the filtered dataframe
st.dataframe(df)

# Pie chart for Category
if 'Category' in df.columns:
    st.write("Gráfico de pastel de la columna Category") # Added heading
    fig, ax = plt.subplots()
    df['Category'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
    st.pyplot(fig)
else:
    st.write("La columna 'Category' no está presente en el DataFrame.")

fig = px.scatter(df, x="total_bill", y="tip", trendline="ols")




# prompt: usando de dataframe df, crear 2 filtros con streamlit, uno con la columna Region y otro con la columna State el filtro de la columna state debe cambiar cuando el filtro de la columna region cambia, e imprimir el dataframe. Tambien crea una grafica de pastel con la columna Category

# Sidebar with filters
st.sidebar.header("Filtros")

# Region filter
selected_regions = st.sidebar.multiselect("Selecciona regiones", df['Region'].unique())

# State filter (dependent on Region)
if selected_regions:
    available_states = df[df['Region'].isin(selected_regions)]['State'].unique()
    selected_states = st.sidebar.multiselect("Selecciona estados", available_states)
else:
    selected_states = st.sidebar.multiselect("Selecciona estados", df['State'].unique())

# Apply filters
if selected_regions:
    df = df[df['Region'].isin(selected_regions)]
if selected_states:
    df = df[df['State'].isin(selected_states)]

# Display the filtered dataframe
st.dataframe(df)

# Pie chart for Category (improved error handling)
if 'Category' in df.columns:
    st.write("Gráfico de pastel de la columna Category")
    if not df['Category'].empty:  # Check if the 'Category' column is not empty after filtering
      fig, ax = plt.subplots()
      df['Category'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
      st.pyplot(fig)
    else:
      st.write("La columna 'Category' está vacía después de aplicar los filtros.")
else:
    st.write("La columna 'Category' no está presente en el DataFrame.")





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
    options=df['region'].unique(),
    default=df['region'].unique()
)

# Filtrar el DataFrame basado en la selección del usuario para 'Region'
df_filtrado_region = df[df['region'].isin(region_seleccionada)]

state_seleccionado = st.sidebar.multiselect(
    'Selecciona uno o más estados',
    options=df_filtrado_region['estado'].unique(),
    default=df_filtrado_region['estado'].unique()
)

# Filtrar el DataFrame basado en la selección del usuario para 'Region' y 'State'
df_filtrado = df[(df['region'].isin(region_seleccionada)) & (df['estado'].isin(state_seleccionado))]

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




# prompt: crea una grafica de pastel de las categorias de los productos y agregale filtros

# ... (your existing code) ...

# Sidebar with filters
st.sidebar.header("Filtros")

# Region filter
selected_regions = st.sidebar.multiselect("Selecciona regiones", df['Region'].unique())

# State filter (dependent on Region)
if selected_regions:
    available_states = df[df['Region'].isin(selected_regions)]['State'].unique()
    selected_states = st.sidebar.multiselect("Selecciona estados", available_states)
else:
    selected_states = st.sidebar.multiselect("Selecciona estados", df['State'].unique())

# Category filter (added)
selected_categories = st.sidebar.multiselect("Selecciona categorías", df['Category'].unique())


# Apply filters
if selected_regions:
    df = df[df['Region'].isin(selected_regions)]
if selected_states:
    df = df[df['State'].isin(selected_states)]
if selected_categories:  # Apply category filter
    df = df[df['Category'].isin(selected_categories)]


# Display the filtered dataframe
st.dataframe(df)

# Pie chart for Category (improved error handling and filtering)
if 'Category' in df.columns:
    st.write("Gráfico de pastel de la columna Category")
    if not df.empty and not df['Category'].empty:  # Check if the DataFrame and 'Category' column are not empty
        category_counts = df['Category'].value_counts()
        if not category_counts.empty: # Check if there are any categories after filtering
          fig, ax = plt.subplots()
          category_counts.plot.pie(autopct='%1.1f%%', ax=ax)
          st.pyplot(fig)
        else:
          st.write("No hay categorías disponibles después de aplicar los filtros.")
    else:
        st.write("El DataFrame o la columna 'Category' está vacía después de aplicar los filtros.")
else:
    st.write("La columna 'Category' no está presente en el DataFrame.")



