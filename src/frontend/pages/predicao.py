import streamlit as st
import requests
import pandas as pd

st.set_page_config(layout="wide")
st.title("📊 Análise Preditiva")

response = requests.get("http://backend:8080/v1/farmtech/predicao", timeout=300) # Adicionado timeout

