import json
from models.profissional import Profissional


class ProfissionalDAO:
    profissionais = []
    @staticmethod
    def abrir():
        try:
            with open("profissionais.json", "r", encoding="utf-8") as f:
                dados = json.load(f)
                ProfissionalDAO.profissionais = [Profissional(**d) for d in dados]
        except FileNotFoundError:
            ProfissionalDAO.profissionais = []
        except json.JSONDecodeError:
            ProfissionalDAO.profissionais = []
    @staticmethod
    def salvar():
       
        with open("profissionais.json", "w", encoding="utf-8") as f:
            dados = [vars(p) for p in ProfissionalDAO.profissionais]
            json.dump(dados, f, indent=4, ensure_ascii=False)
    @staticmethod
    def inserir(profissional):
        ProfissionalDAO.abrir()
        if len(ProfissionalDAO.profissionais) == 0:
            profissional.id = 1
        else:
            profissional.id = ProfissionalDAO.profissionais[-1].id + 1
        ProfissionalDAO.profissionais.append(profissional)
        ProfissionalDAO.salvar()
    @staticmethod
    def listar():
        ProfissionalDAO.abrir()
        return ProfissionalDAO.profissionais
