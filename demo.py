import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Lee el archivo Excel 
try:
    df = pd.read_excel('SalidaFinal.xlsx')
    st.dataframe(df) # Muestra el DataFrame en Streamlit
except FileNotFoundError:
    st.error("Error: Archivo 'SalidaFinal.xlsx' no encontrado. Verifica la ruta.")
except Exception as e:
    st.error(f"Ocurrió un error: {e}")

# Verificar los nombres de las columnas
st.write("Columnas del DataFrame:", df.columns)

# prompt: arma un gráfica de las Sales por Region del dataframe df y mostrar en streamlit

try:
    # Verifica si las columnas 'Sales' y 'Region' existen en el DataFrame
    if 'Sales' in df.columns and 'Region' in df.columns:
        # Crear una gráfica de barras
        plt.figure(figsize=(10, 6))  # Ajusta el tamaño de la figura según sea necesario
        sns.barplot(x='Region', y='Sales', data=df)
        plt.title('Sales por Region')
        plt.xlabel('Region')
        plt.ylabel('Sales')
        plt.xticks(rotation=45, ha='right') # Rota las etiquetas del eje x para mejor legibilidad
        plt.tight_layout() # Ajusta el diseño para evitar que las etiquetas se superpongan

        # Muestra la gráfica en Streamlit
        st.pyplot(plt)
    else:
        st.error("Error: Las columnas 'Sales' o 'Region' no se encuentran en el DataFrame.")

except FileNotFoundError:
    st.error("Error: Archivo 'SalidaFinal.xlsx' no encontrado. Verifica la ruta.")

except Exception as e:
    st.error(f"Ocurrió un error: {e}")

# Crear un filtro de selección múltiple basado en la columna 'Region'
if 'Region' in df.columns:
    region_seleccionada = st.multiselect(
        'Selecciona una o más regiones',
        options=df['Region'].unique(),
        default=df['Region'].unique()
    )

    # Filtrar el DataFrame basado en la selección del usuario
    df_filtrado = df[df['Region'].isin(region_seleccionada)]

    # Mostrar el DataFrame filtrado
    st.write('DataFrame Filtrado:')
    st.dataframe(df_filtrado)
else:
    st.error("Error: La columna 'Region' no se encuentra en el DataFrame.")
import streamlit as st
import pandas as pd
import plotly.express as px

# Simulación de un DataFrame
data = {
    "Region": ["North", "North", "South", "South", "East", "East", "West", "West"],
    "State": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Category": ["Tech", "Furniture", "Office Supplies", "Tech", "Furniture", "Office Supplies", "Tech", "Furniture"],
    "Sales": [100, 200, 150, 300, 250, 400, 350, 500]
}
df = pd.DataFrame(data)

# Filtro por Región
region = st.selectbox("Selecciona una Región", options=["Todas"] + list(df["Region"].unique()))

# Filtrar el DataFrame por Región
if region != "Todas":
    filtered_df = df[df["Region"] == region]
else:
    filtered_df = df

# Filtro por Estado (dependiente de Región)
state = st.selectbox("Selecciona un Estado", options=["Todos"] + list(filtered_df["State"].unique()))

# Filtrar el DataFrame por Estado
if state != "Todos":
    final_df = filtered_df[filtered_df["State"] == state]
else:
    final_df = filtered_df

# Mostrar el DataFrame filtrado
st.write("DataFrame Filtrado:")
st.dataframe(final_df)

# Gráfica de pastel: Distribución de Ventas por Categoría
if not final_df.empty:
    pie_fig = px.pie(final_df, names="Category", values="Sales", title="Distribución de Ventas por Categoría")
    st.plotly_chart(pie_fig)
else:
    st.write("No hay datos para mostrar en la gráfica de pastel.")

# Gráfica de barras: Ventas Acumuladas por Región
region_sales = df.groupby("Region")["Sales"].sum().reset_index()
bar_fig = px.bar(region_sales, x="Region", y="Sales", title="Ventas Acumuladas por Región", labels={"Sales": "Ventas", "Region": "Región"})
st.plotly_chart(bar_fig)



import streamlit as st
import pandas as pd
import plotly.express as px

# Lee el archivo Excel
try:
    df = pd.read_excel('SalidaFinal.xlsx')
    st.dataframe(df)  # Muestra el DataFrame en Streamlit

    # Verifica si las columnas necesarias existen en el DataFrame
    if 'Order Date' in df.columns and 'Sales' in df.columns:
        # Convertir la columna 'Order Date' a formato datetime
        df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

        # Filtrar filas con fechas válidas
        df = df.dropna(subset=['Order Date'])

        # Crear una nueva columna para el año
        df['Year'] = df['Order Date'].dt.year

        # Agrupar por año y calcular el acumulado de ventas
        sales_by_year = df.groupby('Year')['Sales'].sum().reset_index()

        # Crear la gráfica de línea
        line_fig = px.line(
            sales_by_year,
            x='Year',
            y='Sales',
            title='Acumulado de Ventas por Año',
            labels={'Year': 'Año', 'Sales': 'Ventas Acumuladas'}
        )

        # Mostrar la gráfica en Streamlit
        st.plotly_chart(line_fig)
    else:
        st.error("Error: Las columnas 'Order Date' o 'Sales' no se encuentran en el DataFrame.")

except FileNotFoundError:
    st.error("Error: Archivo 'SalidaFinal.xlsx' no encontrado. Verifica la ruta.")

except Exception as e:
    st.error(f"Ocurrió un error: {e}")

import streamlit as st
import pandas as pd
import plotly.express as px

# Lee el archivo Excel
try:
    df = pd.read_excel('SalidaFinal.xlsx')
    st.dataframe(df)  # Muestra el DataFrame en Streamlit

    # Verifica si las columnas necesarias existen en el DataFrame
    if 'Order Date' in df.columns and 'Sales' in df.columns and 'Category' in df.columns:
        # Convertir la columna 'Order Date' a formato datetime
        df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

        # Filtrar filas con fechas válidas
        df = df.dropna(subset=['Order Date'])

        # Crear una nueva columna para el año
        df['Year'] = df['Order Date'].dt.year

        # Agrupar por año y categoría, y calcular el acumulado de ventas
        sales_by_year_category = df.groupby(['Year', 'Category'])['Sales'].sum().reset_index()

        # Crear la gráfica de línea
        line_fig = px.line(
            sales_by_year_category,
            x='Year',
            y='Sales',
            color='Category',  # Desglosar por categoría
            title='Acumulado de Ventas por Año y Categoría',
            labels={'Year': 'Año', 'Sales': 'Ventas Acumuladas', 'Category': 'Categoría'}
        )

        # Mostrar la gráfica en Streamlit
        st.plotly_chart(line_fig)
    else:
        st.error("Error: Las columnas 'Order Date', 'Sales' o 'Category' no se encuentran en el DataFrame.")

except FileNotFoundError:
    st.error("Error: Archivo 'SalidaFinal.xlsx' no encontrado. Verifica la ruta.")

except Exception as e:
    st.error(f"Ocurrió un error: {e}")
