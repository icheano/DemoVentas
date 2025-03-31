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
