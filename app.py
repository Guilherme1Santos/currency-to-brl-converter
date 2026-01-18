import streamlit as st
import requests


def searchCurrency(currency):
    url = f'https://economia.awesomeapi.com.br/last/{currency}-BRL'
    req = requests.get(url)
    value = req.json()[f"{currency}BRL"]["bid"] if req.status_code == 200 else "Moeda não encontrada!"
    return f'R${value}'

st.title("Conversor de moedas")

options = ['DOLLAR', 'EURO', 'BITCOIN']
currencyName = st.selectbox('ESCOLHA UMA DAS OPÇÕES', options)
button = st.button("Pesquisar")


DOLLAR = 'USD'
EURO = 'EUR'
BITCOIN = 'BITCOIN'
if button:
    match currencyName:
        case 'DOLLAR':
            currency = searchCurrency('USD')
            st.success("VALOR ATUAL: ")
            st.text(currency)
    match currencyName:
        case 'EURO':
            currency = searchCurrency('EUR')
            st.success("VALOR ATUAL: ")
            st.text(currency)
    match currencyName:
        case 'BITCOIN':
            currency = searchCurrency('BTC')
            st.success("VALOR ATUAL: ")
            st.text(currency)