import streamlit as st
import requests

st.title("Dashboard Unificado")

res = requests.get("http://localhost:8080/v1/fase1/hello")

if res.status_code == 200:
    st.write("Fase 1:", res.json()["message"])
else:
    st.write("Erro ao acessar a API da Fase 1")
