import os
import Telas as Tela

while True:
    print("\nSistema de Gerenciamento da Biblioteca")
    print("1. Menu de livros")
    print("2. Menu de empréstimos")
    print("3. Menu de usuários")
    print("4. Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        Tela.limpar_tela()
        Tela.abrir_menu_livros()
    elif opcao == 2:
        Tela.limpar_tela()
        Tela.abrir_menu_emprestimos()
    elif opcao == 3:
        Tela.limpar_tela()
        Tela.abrir_menu_usuarios()
    elif opcao == 4:
        Tela.limpar_tela()
        print("Encerrando o sistema...")
        break
    else:
        Tela.limpar_tela()
        print("Digite uma opção válida!")