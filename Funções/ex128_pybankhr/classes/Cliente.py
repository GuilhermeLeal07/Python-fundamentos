class Cliente:
    """Representa um cliente do sistema bancário."""
    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
