import streamlit as st
import requests

st.title("Dashboard Unificado")

fase1_response = requests.get("http://localhost:8080/v1/fase1/hello")

if fase1_response.status_code == 200:
    st.write("Fase 1:", fase1_response.json()["message"])
else:
    st.write("Erro ao acessar a API da Fase 1")
