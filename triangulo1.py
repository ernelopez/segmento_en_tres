import streamlit as st
import numpy as np
import pandas as pd

st.title("Simulación: partir un segmento y formar un triángulo")

# entrada del usuario
n = st.number_input(
    "Cantidad de ensayos",
    min_value=1,
    step=1,
    value=1000
)

# simulación
x = np.random.rand(n)
y = np.random.rand(n)

a = np.minimum(x, y)
b = np.maximum(x, y)

l1 = a
l2 = b - a
l3 = 1 - b

# condición de triángulo
forma_triangulo = np.maximum.reduce([l1, l2, l3]) < 0.5

# tabla
df = pd.DataFrame({
    "x": x,
    "y": y,
    "l1": l1,
    "l2": l2,
    "l3": l3,
    "¿Triángulo?": np.where(forma_triangulo, "✔", "✘")
})

st.subheader("Resultados de los ensayos")
st.dataframe(df)

# probabilidad estimada
prob = forma_triangulo.mean()

st.subheader("Probabilidad estimada")
st.write(f"{prob:.5f}  ({forma_triangulo.sum()} / {n})")
