import streamlit as st
import pandas as pd

# Lee el archivo Excel 
try:
  df = pd.read_excel('SalidaFinal.xlsx')
  st.dataframe(df) # Muestra el DataFrame en Streamlit
except FileNotFoundError:
  st.error("Error: Archivo 'SalidaFinal.xlsx' no encontrado. Verifica la ruta.")
except Exception as e:
  st.error(f"Ocurrió un error: {e}")
# prompt: arma un gráfica de las ventas por Region del dataframe df y mostrar en streamlit

import pandas as pd
import streamlit as st
import plotly.express as px

# Asegúrate de que el archivo 'SalidaFinal.xlsx' esté en el mismo directorio que tu script de Streamlit o proporciona la ruta completa.
try:
    df = pd.read_excel('SalidaFinal.xlsx')
    
    # Verificar si las columnas necesarias existen
    if 'Region' not in df.columns or 'Ventas' not in df.columns:
        st.error("Error: El DataFrame no contiene las columnas 'Region' o 'Ventas'.")
    else:
        # Agrupar las ventas por región
        ventas_por_region = df.groupby('Region')['Ventas'].sum().reset_index()

        # Crear la gráfica con Plotly Express
        fig = px.bar(ventas_por_region, x='Region', y='Ventas', 
                     title='Ventas por Región',
                     labels={'Ventas': 'Total de Ventas', 'Region': 'Región'})

        # Mostrar la gráfica en Streamlit
        st.plotly_chart(fig)

except FileNotFoundError:
    st.error("Error: Archivo 'SalidaFinal.xlsx' no encontrado. Verifica la ruta.")
except Exception as e:
    st.error(f"Ocurrió un error: {e}")
