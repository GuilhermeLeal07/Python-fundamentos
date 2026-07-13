from classes.Cliente import Cliente
from classes.Conta import Conta
from classes.ContaEspecial import ContaEspecial
from classes.ContaRemuneradaPoupanca import ContaRemuneradaPoupanca


cliente1 = Cliente('123', 'Gui', 'Rua X')
cliente2 = Cliente('124', 'Val', 'Rua Y')
cliente3 = Cliente('125', 'Joao', 'Rua Z')

conta1 = Conta(cliente1, 1, 2000)
conta2 = Conta(cliente2, 2, 2000)
conta3 = ContaRemuneradaPoupanca(cliente3, 3, 2000, 10)

conta3.remuneraConta()
conta3.gerar_saldo()
