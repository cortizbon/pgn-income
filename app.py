import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title("Ingresos del PGN")

df = pd.read_csv('income.csv')

st.dataframe(df)

fig, ax = plt.subplots(1, 1, figsize=(14, 8))

df.groupby('year')['Valor'].sum().plot(kind='line', ax=ax)

st.pyplot(fig)