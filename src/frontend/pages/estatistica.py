import streamlit as st
import requests
import pandas as pd

st.title("Resultados da Análise Estatística (R)")

if st.button("Executar análise R"):
    res = requests.get("http://localhost:8080/v1/analises/r/executar")
    if res.status_code == 200:
        st.success("Análise executada com sucesso")
        st.text(res.json()["output"])
    else:
        st.error("Erro ao executar o script R")