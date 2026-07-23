class Extrato:
    """Armazena e exibe o histórico de transações de uma conta."""

    def __init__(self):
        self.transacoes = []

    def gerar_extrato(self, conta):
        """Exibe todas as transações realizadas na conta."""

        print(f'Extrato da conta {conta.numero}')
        print('-' * 42)

        for transacao in self.transacoes:
            print(
                f'{transacao[0]:15s}'
                f'R$ {transacao[1]:10.2f}  '
                f'{transacao[2].strftime("%d/%m/%Y")}'
            )

        print('-' * 42)
        print(f'Saldo atual: R$ {conta.saldo:.2f}')
