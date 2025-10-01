import streamlit as st
import pandas as pd
import time
from views import View


class ManterClienteUI:
    def main():
        st.header("Cadastro de Clientes")
        aba1, aba2, aba3, aba4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with aba1: ManterClienteUI.listar()
        with aba2: ManterClienteUI.inserir()
        with aba3: ManterClienteUI.atualizar()
        with aba4: ManterClienteUI.excluir()


    def listar():
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            tabela = [c.to_json() for c in clientes]
            df = pd.DataFrame(tabela)
            st.dataframe(df)


    def inserir():
        nome = st.text_input("Nome do cliente")
        email = st.text_input("E-mail do cliente")
        fone = st.text_input("Telefone do cliente")
        if st.button("Inserir Cliente"):
            View.cliente_inserir(nome, email, fone)
            st.success("Cliente cadastrado!")
            time.sleep(1)
            st.rerun()


    def atualizar():
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Escolha um cliente", clientes, format_func=lambda c: c.nome)
            nome = st.text_input("Novo nome", op.nome)
            email = st.text_input("Novo e-mail", op.email)
            fone = st.text_input("Novo telefone", op.fone)
            if st.button("Atualizar Cliente"):
                View.cliente_atualizar(op.id, nome, email, fone)
                st.success("Cliente atualizado!")


    def excluir():
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Escolha um cliente para excluir", clientes, format_func=lambda c: c.nome)
            if st.button("Excluir Cliente"):
                View.cliente_excluir(op.id)
                st.success("Cliente excluído")



