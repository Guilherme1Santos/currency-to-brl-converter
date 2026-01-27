import streamlit as st
from services.greatestValue import searchCurrency
from services.FormatBRL import format_brl

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
            st.text(format_brl(currency["atual"]))
            st.metric("Maior valor das ultimas 24 horas:", f"R${currency['max_24h']}")
    match currencyName:
        case 'EURO':
            currency = searchCurrency('EUR')
            st.success("VALOR ATUAL: ")
            st.text(format_brl(currency["atual"]))
            st.metric("Maior valor das ultimas 24 horas:", f"R${currency['max_24h']}")
    match currencyName:
        case 'BITCOIN':
            currency = searchCurrency('BTC')
            st.success("VALOR ATUAL: ")
            st.text(format_brl(currency["atual"]))
            st.metric("Maior valor das ultimas 24 horas:", f"R${currency['max_24h']}")