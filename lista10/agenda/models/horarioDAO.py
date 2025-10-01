import json
from models.horario import Horario


class HorarioDAO:
    horarios = []


    @staticmethod
    def inserir(horario):
        HorarioDAO.abrir()
        if len(HorarioDAO.horarios) == 0:
            horario.id = 1
        else:
            horario.id = HorarioDAO.horarios[-1].id + 1
        HorarioDAO.horarios.append(horario)
        HorarioDAO.salvar()


    @staticmethod
    def listar():
        HorarioDAO.abrir()
        return HorarioDAO.horarios


    @staticmethod
    def atualizar(horario):
        HorarioDAO.abrir()
        for i, h in enumerate(HorarioDAO.horarios):
            if h.id == horario.id:
                HorarioDAO.horarios[i] = horario
        HorarioDAO.salvar()


    @staticmethod
    def excluir(id):
        HorarioDAO.abrir()
        HorarioDAO.horarios = [h for h in HorarioDAO.horarios if h.id != id]
        HorarioDAO.salvar()


    @staticmethod
    def abrir():
        HorarioDAO.horarios = []
        try:
            with open("horarios.json", "r") as f:
                dados = json.load(f)
                for dic in dados:
                    HorarioDAO.horarios.append(Horario.from_json(dic))
        except FileNotFoundError:
            pass


    @staticmethod
    def salvar():
        with open("horarios.json", "w") as f:
            dados = [h.to_json() for h in HorarioDAO.horarios]
            json.dump(dados, f)
