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
