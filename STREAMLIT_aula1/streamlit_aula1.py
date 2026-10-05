import streamlit as st
import pandas as pd

st.title("Meu primeiro dash")

st.subheader("Caio de Noronha Castro Arruda")

nome = "Caio de Noronha Castro Arruda"
idade = 17
st.write(f"Olá, mundo! Meu nome é {nome} e eu tenho {idade} anos.")

df = pd.DataFrame({
    'Matérias': ['Português', 'Matemática', 'Python', 'Frame'],
    'Notas': [5, 9, 7, 10]
})

st.write("### Tabela de Notas")
st.dataframe(df)
st.divider()

st.header("Calculadora de Supermercado")

produtos = {
    "Arroz (5kg)": 25.00,
    "Feijão (1kg)": 8.50,
    "Leite (1L)": 5.20,
    "Café (500g)": 18.00,
    "Açúcar (1kg)": 4.50
}

produto_selecionado = st.selectbox("Selecione um item do supermercado:", list(produtos.keys()))
quantidade = st.number_input("Quantidade:", min_value=1, value=1, step=1)

def calcular_preco(produto, qtd):
    preco_unitario = produtos[produto]
    return preco_unitario * qtd

total = calcular_preco(produto_selecionado, quantidade)
st.success(f"**Total a pagar:** R$ {total:.2f}")