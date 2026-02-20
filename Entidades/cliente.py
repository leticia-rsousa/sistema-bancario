# Aplicação Full-Stack de Sistema Bancário em Python com POO
# Módulo da Entidade Cliente

# Define a classe Cliete
class Cliente:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf

        # Lista vazia para armazenar as contas associadas ao cliente
        self.contas = []

    # Método para adicionar uma conta à lista de contas do cliente
    def adicionar_conta(self, conta):
        self.contas.append(conta)

    # Método que define a representação em string do objeto
    def __str__(self):
        return f"Cliente: {self.nome} | CPF: {self.cpf}"