from models.cliente import Cliente
from models.clienteDAO import ClienteDAO
from models.servico import Servico
from models.servicoDAO import ServicoDAO
from models.profissional import Profissional
from models.profissionalDAO import ProfissionalDAO
from models.horario import Horario
from models.horarioDAO import HorarioDAO


class View:
    
    def cliente_listar(): 
        return ClienteDAO.listar()
    
    def cliente_inserir(nome, email, fone): 
        ClienteDAO.inserir(Cliente(0, nome, email, fone))
    
    def cliente_atualizar(id, nome, email, fone): 
        ClienteDAO.atualizar(Cliente(id, nome, email, fone))
    
    def cliente_excluir(id): 
        ClienteDAO.excluir(id)


    
    def servico_listar(): 
        return ServicoDAO.listar()
    
    def servico_inserir(descricao, valor): 
        ServicoDAO.inserir(Servico(0, descricao, valor))
    
    def servico_atualizar(id, descricao, valor): 
        ServicoDAO.atualizar(Servico(id, descricao, valor))
    
    def servico_excluir(id): 
        ServicoDAO.excluir(id)


    
    def profissional_listar(): 
        return ProfissionalDAO.listar()
    
    def profissional_inserir(nome, especialidade, fone): 
        ProfissionalDAO.inserir(Profissional(0, nome, especialidade, fone))
    
    def profissional_atualizar(id, nome, especialidade, fone): 
        ProfissionalDAO.atualizar(Profissional(id, nome, especialidade, fone))
    
    def profissional_excluir(id): 
        ProfissionalDAO.excluir(id)


    
    def horario_listar(): 
        return HorarioDAO.listar()
    
    def horario_inserir(data, hora, idProfissional): 
        HorarioDAO.inserir(Horario(0, data, hora, idProfissional))
    
    def horario_atualizar(id, data, hora, idProfissional): 
        HorarioDAO.atualizar(Horario(id, data, hora, idProfissional))
    
    def horario_excluir(id): 
        HorarioDAO.excluir(id)




    
