import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import datetime 

#1. Configuración inicial de la aplicación
st.set_page_config(
  page_title="Producción agroindustrial",
  page_icon="🌳",
  layout="wide"
)
st.title("🌳 Principal producción Agroindustrial en Colombia 🌳")
st.sidebar.title("🔍 Opciones")

# 2. Generación de Datos Aleatorios
data = pd.DataFrame({
    "Fecha": pd.date_range(start="2024-01-01", periods=150, freq="D"),
    "Producto": np.random.choice(["Café", "Cacao", "Palma de Aceite", "Banano", "Azúcar", "Aguacate", "Flores", "Leche"], size=150),
    "Región": np.random.choice(["Huila", "Antioquia", "Cauca", "Meta", "Santander", "Valle del Cauca", "Cundinamarca", "Magdalena"], size=150),
    "Producción (ton)": np.random.randint(500, 10000, size=150),  # Toneladas producidas
    "Exportaciones (USD)": np.random.randint(50000, 5000000, size=150),  # Valor en dólares
    "Procesamiento": np.random.choice(["Tostado", "Fermentación", "Extracción de aceite", "Empaque", "Refinamiento", "Pasteurización"], size=150),
    "Empleo Generado": np.random.randint(50, 5000, size=150),  # Número de empleos
    "Costo de Producción (USD)": np.random.randint(10000, 1000000, size=150)  # Costos de producción
})

# 3. Implementación de la Barra de Navegación
menu = st.sidebar.radio(
    "Selecciona una opción:",
    ["Inicio", "Datos", "Visualización", "Configuración"]
)

# 4. Mostrar los Datos
if menu == "Datos":
    st.subheader("📂 Datos Generados")
    st.dataframe(data)

# 5. Filtrar por Categoría
filtered_data = data  # Asegurar que filtered_data esté definido en todo el script
if menu == "Visualización":
    st.subheader("📊 Visualización de Datos")
    categoria = st.sidebar.selectbox("Selecciona una categoría", data["Categoría"].unique())
    filtered_data = data[data["Categoría"] == categoria]
    st.write(f"Mostrando datos para la categoría {categoria}")
    st.dataframe(filtered_data)

    # 6. Filtrar por Ventas
    ventas_min, ventas_max = st.sidebar.slider(
        "Selecciona el rango de ventas:",
        min_value=int(data["Ventas"].min()),
        max_value=int(data["Ventas"].max()),
        value=(int(data["Ventas"].min()), int(data["Ventas"].max()))
    )
    filtered_data = filtered_data[(filtered_data["Ventas"] >= ventas_min) & (filtered_data["Ventas"] <= ventas_max)]

    # 7. Filtrar por Fecha
    fecha_inicio, fecha_fin = st.sidebar.date_input(
        "Selecciona el rango de fechas:",
        [data["Fecha"].min(), data["Fecha"].max()],
        min_value=data["Fecha"].min(),
        max_value=data["Fecha"].max()
    )
    filtered_data = filtered_data[(filtered_data["Fecha"] >= pd.to_datetime(fecha_inicio)) & (filtered_data["Fecha"] <= pd.to_datetime(fecha_fin))]
