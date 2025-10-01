
class Profissional:
    def __init__(self, id, nome, especialidade, fone):
        self.id = id
        self.nome = nome
        self.especialidade = especialidade
        self.fone = fone


    def __str__(self):
        return f"{self.id} - {self.nome} ({self.especialidade}) - {self.fone}"


    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "especialidade": self.especialidade,
            "fone": self.fone
        }


    @staticmethod
    def from_json(dic):
        return Profissional(dic["id"], dic["nome"], dic["especialidade"], dic["fone"])



