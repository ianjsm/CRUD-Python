import sys
import os

import Telas

while True:
    print("\nSistema de Gerenciamento da Biblioteca")
    print("1. Menu de livros")
    print("2. Menu de empréstimos")
    print("3. Menu de usuários")
    print("4. Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        Telas.limpar_tela()
        Telas.abrir_menu_livros()
    elif opcao == 2:
        Telas.limpar_tela()
        Telas.abrir_menu_emprestimos()
    elif opcao == 3:
        Telas.limpar_tela()
        Telas.abrir_menu_usuarios()
    elif opcao == 4:
        Telas.limpar_tela()
        print("Encerrando o sistema...")
        break
    else:
        Telas.limpar_tela()
        print("Digite uma opção válida!")