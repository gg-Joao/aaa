
import streamlit as st
import pandas as pd
import time
from views import View


class ManterHorarioUI:
    def main():
        st.header("Cadastro de Horários")
        aba1, aba2, aba3, aba4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])


        with aba1: ManterHorarioUI.listar()
        with aba2: ManterHorarioUI.inserir()
        with aba3: ManterHorarioUI.atualizar()
        with aba4: ManterHorarioUI.excluir()


    def listar():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            # mostrar nome do profissional junto
            profissionais = {p.id: p.nome for p in View.profissional_listar()}
            tabela = []
            for h in horarios:
                dic = h.to_json()
                dic["profissional"] = profissionais.get(h.idProfissional, "N/A")
                tabela.append(dic)
            df = pd.DataFrame(tabela)
            st.dataframe(df)


    def inserir():
        data = st.text_input("Data (dd/mm/aaaa)")
        hora = st.text_input("Hora (hh:mm)")
        profissionais = View.profissional_listar()
        if len(profissionais) == 0:
            st.warning("Cadastre primeiro um profissional!")
        else:
            profissional = st.selectbox("Profissional", profissionais, format_func=lambda p: p.nome)
            if st.button("Inserir Horário"):
                View.horario_inserir(data, hora, profissional.id)
                st.success("Horário cadastrado!")
                time.sleep(1)
                st.rerun()


    def atualizar():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            op = st.selectbox("Escolha um horário", horarios, format_func=lambda h: f"{h.data} {h.hora}")
            data = st.text_input("Nova data", op.data)
            hora = st.text_input("Nova hora", op.hora)
            profissionais = View.profissional_listar()
            profissional = st.selectbox("Profissional", profissionais, index=0, format_func=lambda p: p.nome)
            if st.button("Atualizar Horário"):
                View.horario_atualizar(op.id, data, hora, profissional.id)
                st.success("Horário atualizado!")


    def excluir():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            op = st.selectbox("Escolha um horário para excluir", horarios, format_func=lambda h: f"{h.data} {h.hora}")
            if st.button("Excluir Horário"):
                View.horario_excluir(op.id)
                st.success("Horário excluído")


