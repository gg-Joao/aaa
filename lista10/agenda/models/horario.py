class Horario:
    def __init__(self, id, data, hora, idProfissional):
        self.id = id
        self.data = data
        self.hora = hora
        self.idProfissional = idProfissional


    def __str__(self):
        return f"{self.id} - {self.data} {self.hora} - Profissional {self.idProfissional}"


    def to_json(self):
        return {
            "id": self.id,
            "data": self.data,
            "hora": self.hora,
            "idProfissional": self.idProfissional
        }


    @staticmethod
    def from_json(dic):
        return Horario(dic["id"], dic["data"], dic["hora"], dic["idProfissional"])



