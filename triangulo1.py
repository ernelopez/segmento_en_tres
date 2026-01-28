import streamlit as st
import numpy as np
import pandas as pd

st.title("Simulación: partir un segmento y formar un triángulo")

# input
n = st.number_input(
    "Cantidad de ensayos",
    min_value=1,
    max_value=10,
    step=1,
    value=1
)

# inicializar estado
if "df" not in st.session_state:
    st.session_state.df = None
    st.session_state.prob = None

# botón
if st.button("Ejecutar simulación"):
    x = np.random.rand(n)
    y = np.random.rand(n)

    a = np.minimum(x, y)
    b = np.maximum(x, y)

    l1 = a
    l2 = b - a
    l3 = 1 - b

    forma_triangulo = np.maximum.reduce([l1, l2, l3]) < 0.5

    st.session_state.df = pd.DataFrame({
        "Corte 1": x,
        "Corte 2": y,
        "Lado 1": l1,
        "Lado 2": l2,
        "Lado 3": l3,
        "¿Triángulo?": np.where(forma_triangulo, "✔", "✘")
    })

    st.session_state.prob = forma_triangulo.mean()

# salida
if st.session_state.df is not None:
    st.subheader("Resultados de los ensayos")
    st.dataframe(st.session_state.df)

    st.subheader("Probabilidad estimada")
    st.write(
        f"{st.session_state.prob:.5f} "
        f"({(st.session_state.df['¿Triángulo?'] == '✔').sum()} / {n})"
    )
