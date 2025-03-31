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
region = st.selectbox("Selecciona una Región", options=df["Region"].unique())

# Filtrar el DataFrame por Región
filtered_df = df[df["Region"] == region]

# Filtro por Estado (dependiente de Región)
state = st.selectbox("Selecciona un Estado", options=filtered_df["State"].unique())

# Filtrar el DataFrame por Estado
final_df = filtered_df[filtered_df["State"] == state]

# Mostrar el DataFrame filtrado
st.write("DataFrame Filtrado:")
st.dataframe(final_df)

# Crear una gráfica de pastel con la columna Category
fig = px.pie(df, names="Category", values="Sales", title="Distribución de Ventas por Categoría")
st.plotly_chart(fig)


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

# Crear una gráfica de pastel con la columna Category
fig = px.pie(final_df, names="Category", values="Sales", title="Distribución de Ventas por Categoría")
st.plotly_chart(fig)
streamlit run app.py
