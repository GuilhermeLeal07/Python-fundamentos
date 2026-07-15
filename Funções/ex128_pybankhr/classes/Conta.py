import datetime
from classes.Extrato import Extrato


class Conta:
    """Representa uma conta bancária."""

    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()

    def depositar(self, valor):
        """Realiza um depósito na conta."""

        self.saldo += valor
        self.extrato.transacoes.append(['Depósito', valor, datetime.datetime.today()])

    def sacar(self, valor):
        """Realiza um saque, caso haja saldo disponível."""

        if self.saldo < valor:
            print(
                f'Não existe saldo suficiente na conta '
                f'{self.numero} do cliente {self.clientes.cpf}'
            )
            return False

        self.saldo -= valor
        self.extrato.transacoes.append(['Saque', valor, datetime.datetime.today()])
        return True

    def transfere_valor(self, conta_destino, valor):
        """Transfere um valor para outra conta."""

        if self.saldo < valor:
            return 'Não existe saldo suficiente!'

        conta_destino.depositar(valor)
        self.saldo -= valor

        self.extrato.transacoes.append(['Transferência', valor, datetime.datetime.today()])

        return 'Transferência realizada com sucesso!'

    def sacar_saldo(self):
        """Exibe o saldo da conta."""

        print(f'Conta: {self.numero}')
        print(f'Saldo: R$ {self.saldo:.2f}')

    def gerar_saldo(self):
        """Exibe o saldo atual da conta."""

        print(f'Conta: {self.numero}')
        print(f'Saldo atual: R$ {self.saldo:.2f}')
