import streamlit as st
import pandas as pd
import time
from views import View


class ManterProfissionalUI:
    def main():
        st.header("Cadastro de Profissionais")
        aba1, aba2, aba3, aba4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])


        with aba1: ManterProfissionalUI.listar()
        with aba2: ManterProfissionalUI.inserir()
        with aba3: ManterProfissionalUI.atualizar()
        with aba4: ManterProfissionalUI.excluir()


    def listar():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            tabela = [p.to_json() for p in profissionais]
            df = pd.DataFrame(tabela)
            st.dataframe(df)


    def inserir():
        nome = st.text_input("Nome do profissional")
        especialidade = st.text_input("Especialidade")
        fone = st.text_input("Telefone")
        if st.button("Inserir Profissional"):
            View.profissional_inserir(nome, especialidade, fone)
            st.success("Profissional cadastrado!")
            time.sleep(1)
            st.rerun()


    def atualizar():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Escolha um profissional", profissionais, format_func=lambda p: p.nome)
            nome = st.text_input("Novo nome", op.nome)
            especialidade = st.text_input("Nova especialidade", op.especialidade)
            fone = st.text_input("Novo telefone", op.fone)
            if st.button("Atualizar Profissional"):
                View.profissional_atualizar(op.id, nome, especialidade, fone)
                st.success("Profissional atualizado!")


    def excluir():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Escolha um profissional para excluir", profissionais, format_func=lambda p: p.nome)
            if st.button("Excluir Profissional"):
                View.profissional_excluir(op.id)
                st.success("Profissional excluído")


