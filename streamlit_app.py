streamlit run streamlit_app.py 
# prompt: Usando streamlit, crea un filtro usando la columna region del dataframe df y cuando crees esl filtro ponlo dentro de un sitebar

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Asegúrate de que el archivo 'SalidaFinal.xlsx' esté en el mismo directorio que tu script de Streamlit o proporciona la ruta completa.
try:
    df = pd.read_excel('SalidaFinal.xlsx')
except FileNotFoundError:
    st.error("Error: Archivo 'SalidaFinal.xlsx' no encontrado. Verifica la ruta.")
    st.stop()  # Detén la ejecución si el archivo no se encuentra
except Exception as e:
    st.error(f"Ocurrió un error al leer el archivo: {e}")
    st.stop()


# Sidebar con filtro de región
st.sidebar.header("Filtros")
selected_regions = st.sidebar.multiselect("Selecciona regiones", df['Region'].unique())


# Aplicar filtro
if selected_regions:
    df_filtered = df[df['Region'].isin(selected_regions)]
else:
    df_filtered = df  # Mostrar todos los datos si no se selecciona ninguna región

# Mostrar el DataFrame filtrado
st.dataframe(df_filtered)


# Gráfico de barras de ventas por región (usando el DataFrame filtrado)
try:
    if 'Sales' in df_filtered.columns and 'Region' in df_filtered.columns:
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Region', y='Sales', data=df_filtered)
        plt.title('Sales por Region')
        plt.xlabel('Region')
        plt.ylabel('Sales')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        st.pyplot(plt)
    else:
        st.error("Error: Las columnas 'Sales' o 'Region' no se encuentran en el DataFrame.")

except Exception as e:
    st.error(f"Ocurrió un error al generar el gráfico: {e}")

with st.sidebar:
    #Crea un filtro en la columna 'Region'
    region_seleccionada = st.selectbox('Selecciona una Region') , df ['Region'] . unique ())

# prompt: Usando streamlit, crea un filtro usando la columna region del dataframe df y cuando crees esl filtro ponlo dentro de un sitebar

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Asegúrate de que el archivo 'SalidaFinal.xlsx' esté en el mismo directorio que tu script de Streamlit o proporciona la ruta completa.
try:
    df = pd.read_excel('SalidaFinal.xlsx')
except FileNotFoundError:
    st.error("Error: Archivo 'SalidaFinal.xlsx' no encontrado. Verifica la ruta.")
    st.stop()  # Detén la ejecución si el archivo no se encuentra
except Exception as e:
    st.error(f"Ocurrió un error al leer el archivo: {e}")
    st.stop()


# Sidebar con filtro de región
st.sidebar.header("Filtros")
selected_regions = st.sidebar.multiselect("Selecciona regiones", df['Region'].unique())


# Aplicar filtro
if selected_regions:
    df_filtered = df[df['Region'].isin(selected_regions)]
else:
    df_filtered = df  # Mostrar todos los datos si no se selecciona ninguna región

# Mostrar el DataFrame filtrado
st.dataframe(df_filtered)


# Gráfico de barras de ventas por región (usando el DataFrame filtrado)
try:
    if 'Sales' in df_filtered.columns and 'Region' in df_filtered.columns:
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Region', y='Sales', data=df_filtered)
        plt.title('Sales por Region')
        plt.xlabel('Region')
        plt.ylabel('Sales')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        st.pyplot(plt)
    else:
        st.error("Error: Las columnas 'Sales' o 'Region' no se encuentran en el DataFrame.")

except Exception as e:
    st.error(f"Ocurrió un error al generar el gráfico: {e}")
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

#Filtros
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
