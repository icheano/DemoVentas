import streamlit as st
import pandas as pd
import plotly.express as px

#Título
st.title("Mi primer app de streamlit editada")

#Para ejecutar, desde la consola escribimos: streamlit run nombrearhivo.py

#header
st.header("Semestre Sep-Enero 2021")

#Texto
st.text("Herramientas para el análisis de datos")

#Markdown
st.markdown("### Hola")

#Mensajes

st.success("Successful")

st.info("Information!")

st.warning("This is a warning")

st.error("This is an error Danger")

st.text("Lo interesante de streamlit son los widgets:")

valor = st.checkbox("Show/Hide")
# Checkbox
if valor:
    st.text("Showing or Hiding Widget")

# Radio Buttons
status = st.radio("What is your status", ("Active", "Inactive"))

if status == 'Active':
    st.success("You are Active")
else:
    st.warning("Inactive, Activate")

# SelectBox
occupation = st.selectbox(
    "Your Occupation",
    ["Programmer", "DataScientist", "Doctor", "Businessman"])
st.write("You selected this option ", occupation)

# MultiSelect
location = st.multiselect("Where do you work?",
                          ("London", "New York", "Accra", "Kiev", "Nepal"))
st.write("You selected", len(location), "locations")

# Slider
level = st.slider("What is your level", 1, 5)

# Buttons
st.button("Simple Button")

if st.button("About"):
    st.text("Streamlit is Cool")

# SIDEBARS
st.sidebar.header("About")
st.sidebar.text("This is Streamlit Tut")


#Tambien podemos seguir llamando al código de python con el que hemos estado trabajando: pandas, plots, etc,
@st.cache  # Para que los datos solo se descarguen una vez
def get_data():
    url = "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-09-12/visualisations/listings.csv"
    return pd.read_csv(url)


df = get_data()

st.dataframe(df.head())

st.map(df)

values = st.sidebar.slider("Price range", float(df.price.min()), 1000.0,
                           (50.0, 300.0))
st.write(values[1])

f = px.histogram(df[(df.price > int(values[0])) & (df.price < int(values[1]))],
                 x="price",
                 nbins=15,
                 title="Price distribution")
f.update_xaxes(title="Price")
f.update_yaxes(title="No. of listings")
st.plotly_chart(f)







import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Ejemplo de DataFrame
data = {
    'Region': ['Norte', 'Sur', 'Este', 'Oeste', 'Norte', 'Sur', 'Este', 'Oeste'],
    'State': ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D'],
    'Category': ['Cat1', 'Cat2', 'Cat3', 'Cat1', 'Cat2', 'Cat3', 'Cat1', 'Cat2'],
    'Valor': [10, 20, 30, 40, 50, 60, 70, 80]
}
df = pd.DataFrame(data)

# Título de la aplicación
st.title('Filtros de Regiones y Estados')

# Crear filtros de selección múltiple basados en las columnas 'Region' y 'State' y colocarlos en la barra lateral
region_seleccionada = st.sidebar.multiselect(
    'Selecciona una o más regiones',
    options=df['Region'].unique(),
    default=df['Region'].unique()
)

state_seleccionado = st.sidebar.multiselect(
    'Selecciona uno o más estados',
    options=df['State'].unique(),
    default=df['State'].unique()
)

# Filtrar el DataFrame basado en la selección del usuario
df_filtrado = df[(df['Region'].isin(region_seleccionada)) & (df['State'].isin(state_seleccionado))]

# Mostrar el DataFrame filtrado
st.write('DataFrame Filtrado:')
st.dataframe(df_filtrado)

# Crear una gráfica de pastel basada en la columna 'Category'
st.write('Gráfica de Pastel por Categoría:')
categoria_counts = df['Category'].value_counts()

fig, ax = plt.subplots()
ax.pie(categoria_counts, labels=categoria_counts.index, autopct='%1.1f%%')
ax.axis('equal')  # Para asegurar que el pastel es un círculo.

st.pyplot(fig)





import streamlit as st
import pandas as pd

# Cargar el archivo Excel
url = 'https://github.com/icheano/DemoVentas/raw/main/SalidaFinal.xlsx'
df = pd.read_excel(url, sheet_name='Sheet1')

# Título de la aplicación
st.title('Filtros de Regiones y Estados')

# Crear filtros de selección múltiple basados en las columnas 'region' y 'estado' y colocarlos en la barra lateral
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

# Mostrar la gráfica de pastel
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
st.title('Filtros de Regiones y Estados')

# Crear filtros de selección múltiple basados en las columnas 'Region' y 'State' y colocarlos en la barra lateral
region_seleccionada = st.sidebar.multiselect(
    'Selecciona una o más regiones',
    options=df['Region'].unique(),
    default=df['Region'].unique()
)

state_seleccionado = st.sidebar.multiselect(
    'Selecciona uno o más estados',
    options=df['State'].unique(),
    default=df['State'].unique()
)

# Filtrar el DataFrame basado en la selección del usuario
df_filtrado = df[(df['Region'].isin(region_seleccionada)) & (df['State'].isin(state_seleccionado))]

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
