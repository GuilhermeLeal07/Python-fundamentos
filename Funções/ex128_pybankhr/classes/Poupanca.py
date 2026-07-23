class Poupanca:
    """Representa uma conta poupança com taxa de remuneração."""

    def __init__(self, taxa_remuneracao):
        self.taxa_remuneracao = taxa_remuneracao

    def remunera_conta(self):
        """Aplica a taxa de remuneração ao saldo da conta."""

        self.saldo -= self.saldo * self.taxa_remuneracao
