import streamlit as st
import pandas as pd
import time
from views import View


class ManterServicoUI:
    def main():
        st.header("Cadastro de Serviços")
        aba1, aba2, aba3, aba4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with aba1: ManterServicoUI.listar()
        with aba2: ManterServicoUI.inserir()
        with aba3: ManterServicoUI.atualizar()
        with aba4: ManterServicoUI.excluir()


    def listar():
        servicos = View.servico_listar()
        if len(servicos) == 0:
            st.write("Nenhum serviço cadastrado")
        else:
            tabela = [s.to_json() for s in servicos]
            df = pd.DataFrame(tabela)
            st.dataframe(df)


    def inserir():
        descricao = st.text_input("Descrição do serviço")
        valor = st.number_input("Valor (R$)", min_value=0.0, step=0.01)
        if st.button("Inserir Serviço"):
            View.servico_inserir(descricao, valor)
            st.success("Serviço cadastrado!")
            time.sleep(1)
            st.rerun()


    def atualizar():
        servicos = View.servico_listar()
        if len(servicos) == 0:
            st.write("Nenhum serviço cadastrado")
        else:
            op = st.selectbox("Escolha um serviço", servicos, format_func=lambda s: s.descricao)
            descricao = st.text_input("Nova descrição", op.descricao)
            valor = st.number_input("Novo valor", min_value=0.0, step=0.01, value=op.valor)
            if st.button("Atualizar Serviço"):
                View.servico_atualizar(op.id, descricao, valor)
                st.success("Serviço atualizado")


    def excluir():
        servicos = View.servico_listar()
        if len(servicos) == 0:
            st.write("Nenhum serviço cadastrado")
        else:
            op = st.selectbox("Escolha um serviço para excluir", servicos, format_func=lambda s: s.descricao)
            if st.button("Excluir Serviço"):
                View.servico_excluir(op.id)
                st.success("Serviço excluído")


