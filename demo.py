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

matplotlib

# prompt: arma un gráfica de las Sales por Region del dataframe df y mostrar en streamlit

import matplotlib.pyplot as plt
import seaborn as sns

# ... (tu código existente) ...

try:
    df = pd.read_excel('SalidaFinal.xlsx')

    # Verifica si las columnas 'Sales' y 'Region' existen en el DataFrame
    if 'Sales' in df.columns and 'Region' in df.columns:
        # Crea la gráfica
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
