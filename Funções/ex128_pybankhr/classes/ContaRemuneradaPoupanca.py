from classes.Conta import Conta
from classes.Poupanca import Poupanca

class ContaRemuneradaPoupanca(Conta, Poupanca):
    """Representa uma conta poupança remunerada."""

    def __init__(self, clientes, numero, saldo, taxa_remuneracao):
        Conta.__init__(self, clientes, numero, saldo)
        Poupanca.__init__(self, taxa_remuneracao)

    def remunera_conta(self):
        """Aplica a remuneração diária ao saldo da conta."""

        self.saldo += self.saldo * (self.taxa_remuneracao / 30)
