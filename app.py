import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title("Ingresos del PGN")

df = pd.read_csv('income.csv')

st.dataframe(df)