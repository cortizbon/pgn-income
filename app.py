import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title("Ingresos del PGN")

df = pd.read_csv('income.csv')

st.dataframe(df)

fig, ax = plt.subplots(1, 1, figsize=(10, 6))

df.groupby('Año')['Valor'].sum().plot(kind='line', ax=ax)

st.pyplot(fig)

fig, ax = plt.subplots(1, 1, figsize=(10, 6))

df[df['Sector'] == 'Nación'].groupby('Año')['Valor'].sum().plot(kind='line', ax=ax)

st.pyplot(fig)