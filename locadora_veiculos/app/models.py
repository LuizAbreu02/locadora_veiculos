from . import db


# Usuários
    # id_usuario
    # nome
    # senha
    # tipo
    # status

#------------------------------

# Cadastrar()
    # Logar
    # ReservarVeiculo
    # FiltrarVeiculo
    # Verificacao

#----------------------------------------

# Dados_Pessoais
    # id_dadosPessoais
    # nome
    # endereco
    # email
    # dataNascimento
    # rg
    # cpf
    # telefone
    # id_usuario

#----------------------------------

# Veiculo
    # id_veiculo
    # marca
    # modelo
    # categoria
    # ano
    # precoDia
    # disponibilidade

    # marcarIndisponibilidade

class Veiculo(db.model):

    __tablename__ = 'veiculos'

    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(30), nullable=False)
    ano = db.Column(db.String(10), nullable=False)
    precoDia = db.Column(db.Float, nullable=False)
    disponibilidade = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'Veiculo {self.marca}, {self.modelo}, {self.categoria}, {self.ano}, {self.precoDia}, {self.disponibilidade}'

#------------------------------

# Manutencao
    # id_manutencao
    # veiculo
    # descricao
    # dataEntrada
    # dataSaida

    # registrarManutencao()
    # listarManutencao() 


#------------------------------

# Reserva
    # id_reserva
    # cliente
    # veiculo]
    # dataInicio
    # dataFim
    # status

    # confirmarReseva()
    # cancelarReserva()

#----------------------------------------



