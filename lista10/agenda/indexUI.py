import streamlit as st
from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
from templates.manterprofissionalUI import ManterProfissionalUI


class IndexUI:
    def main():
        st.sidebar.title("Menu")
        escolha = st.sidebar.radio("Selecione", ["Clientes", "Serviços", "Profissionais"])
        if escolha == "Clientes":
            ManterClienteUI.main()
        elif escolha == "Serviços":
            ManterServicoUI.main()
        else:
            ManterProfissionalUI.main()




IndexUI.main()
