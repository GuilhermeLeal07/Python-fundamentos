from utilidadesCev.funçoes import titulo, ajuda

def mostra_menu():
    """Exibe o menu principal do sistema."""
    
    titulo('MENU PRINCIPAL')
    print('1 – Ver título')
    print('2 – Ver ajuda de função')
    print('3 – Sair')
    print('~' * 30)

# Programa principal
while True:
    mostra_menu()
    opc = input('Escolha uma opção: ')

    if opc == '1':
        titulo('Você escolheu 1')
      
    elif opc == '2':
        ajuda(titulo)

    elif opc == '3':
        break

    else:
        print('Erro! Digite uma opção válida.')
