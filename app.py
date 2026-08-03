import streamlit as st
import pandas as pd
import plotly.express as px

datos_vehiculos = pd.read_csv("datos/vehicles_us.csv")

st.header("Análisis exploratorio de vehículos usados")

st.write(
    "Esta aplicación permite explorar información de anuncios de vehículos usados. "
    "Puedes visualizar la distribución del odómetro y la relación entre odómetro y precio."
)

mostrar_histograma = st.checkbox("Mostrar histograma del odómetro")

if mostrar_histograma:
    st.write("Histograma de la distribución del odómetro de los vehículos.")

    figura_histograma = px.histogram(
        datos_vehiculos,
        x="odometer",
        title="Distribución del odómetro",
        labels={
            "odometer": "Odómetro",
            "count": "Cantidad de vehículos"
        }
    )

    st.plotly_chart(figura_histograma, use_container_width=True)


mostrar_dispersion = st.checkbox("Mostrar gráfico de dispersión entre odómetro y precio")

if mostrar_dispersion:
    st.write("Gráfico de dispersión entre odómetro y precio.")

    figura_dispersion = px.scatter(
        datos_vehiculos,
        x="odometer",
        y="price",
        title="Relación entre odómetro y precio",
        labels={
            "odometer": "Odómetro",
            "price": "Precio"
        }
    )

    st.plotly_chart(figura_dispersion, use_container_width=True)