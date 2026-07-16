import datetime
from classes.Conta import Conta


class ContaEspecial(Conta):
    """Representa uma conta especial com limite disponível."""

    def __init__(self, clientes, numero, saldo, limite):
        super().__init__(clientes, numero, saldo)
        self.limite = limite

    def sacar(self, valor):
        """Realiza um saque utilizando o saldo e o limite disponível."""

        if (self.saldo + self.limite) < valor:
            print(
                f'Não existe saldo suficiente na conta '
                f'{self.numero} do cliente {self.clientes.cpf}.'
            )
            return False

        self.saldo -= valor

        if self.saldo < 0:
            self.limite += self.saldo

        self.extrato.transacoes.append(
            ['Saque', valor, datetime.datetime.today()]
        )

        return True
