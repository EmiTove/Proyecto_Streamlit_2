import streamlit as st

from data_loader import get_data_api
from api_kpis import plot_kpis
from api_altair import plot_altair_insights
from api_altair import plot_altair_benchmark

st.set_page_config(layout="wide", page_title="Dashboard Pro", page_icon="📊")

# --- SIDEBAR: CONFIGURACIÓN ---
st.sidebar.title("🛠️ Configuración")

#Para generar visualmente un campo donde mostrar el URL
api_url_input = st.sidebar.text_input(
    "URL",
    value="https://restcountries.com/v3.1/all?fields=name,region,population,area,capital,cca3",
)

#Incluir en un dataframe el url extraido para poder trabajar en python
df_api = get_data_api(api_url_input)

#Se extraen los valores unicos de la columna región y se presenta en la opcion de una caja desplegable
region = st.sidebar.selectbox("Región", sorted(df_api["region"].unique())) 

#Se utiliza el filtro en base a lo selecionado en el selectbox
df_api_filtered = df_api[df_api["region"] == region]

#para mostar los encabezados del total de tu data
plot_kpis(df_api)

st.divider()

#Sirve para mostrar encabezados en base al filtro aplicado en la caja
plot_kpis(df_api_filtered)

st.divider()

#para mostrar los campos en base al filtro elegido
st.dataframe(df_api_filtered)

#Para mostrar el primer grafico de altair
plot_altair_insights(df_api_filtered, region)


plot_altair_benchmark( df_api_filtered, region)

st.sidebar.divider()