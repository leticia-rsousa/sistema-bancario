# Aplicação Full-Stack de Sistema Bancário em Python com POO
# Módulo para exceções custumizadas da aplicação

class SaldoInsuficienteError(Exception):
    """ Exceção levantada quando uma operação de saque excede o saldo disponível. """
    def __init__(self, saldo_atual, valor_saque, mensagem = "Saldo insuficiente para realizar o saque."):
        self.saldo_atual = saldo_atual
        self.valor_saque = valor_saque

        # Mensagem detalhada de erro com saldo atual e valor de saque
        self.mensagem = f"{mensagem} Saldo atual: R${saldo_atual:.2f}, Tentativa de saque: R${valor_saque:.2f}"

        # Chama o construtor da classe com Exception com a mensagem
        super().__init__(self.mensagem)

class ContaInexistenteError(Exception):
    """ Exceção levantada ao tentar operar em uma conta que não existe. """
    def __init__(self, numero_conta, mensagem = "A conta especificada não foi encontrada."):
        self.numero_conta = numero_conta

        # Mensagem detalhada de erro com número da conta
        self.mensagem = f"{mensagem} Número da conta: {numero_conta}"

        # Chama o construtor da classe Exception com a mensagem
        super().__init__(self.mensagem)