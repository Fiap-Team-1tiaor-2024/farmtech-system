import streamlit as st
import requests
import pandas as pd

st.title("Resultados da Análise Estatística (R)")

if st.button("Executar análise R"):
    res = requests.post("http://farmtech-backend:8080/v1/farmtech/analises/r/executar")

    if res.status_code == 200:
        try:
            data = res.json()
        except ValueError:
            st.error("Erro: resposta do servidor não está em formato JSON.")
            st.text(res.text)  # Exibe o conteúdo bruto para depuração
        else:
            if "output" in data:
                st.success("Análise executada com sucesso")
                st.text(data["output"])
            elif "error" in data:
                st.error(f"Erro ao executar script R - FRONT:\n{data['error']}")
                if "details" in data:
                    st.text(data["details"])
            else:
                st.warning("Resposta inesperada do servidor:")
                st.json(data)
