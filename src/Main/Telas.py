import os
from Livro import Livro #importação de uma classe
from Emprestimo import Emprestimo
from Usuario import Usuario

def limpar_tela():
    os.system("cls")

def abrir_menu_livros():
    while True:
        print("\n--- Menu de livros ---")
        print("1. Adicionar livro")
        print("2. Remover livro")
        print("3. Visualizar livros")
        print("4. Atualizar livro")
        print("5. Voltar")
        opcao_livros = int(input("Digite a opção desejada: "))
        if opcao_livros == 1: #ADICIONAR LIVROS
            limpar_tela()
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            lancamento = int(input("Digite o ano de lançamento do livro: "))
            Livro.adicionar_livro(titulo, autor, lancamento)
            print("Livro adicionado com sucesso!")
        elif opcao_livros == 2: #REMOVER LIVROS
            limpar_tela()
            print(Livro.visualizar_livros())
            id_livro = int(input("Digite o ID do livro que deseja remover: "))
            Livro.remover_livro(id_livro)
            print("Livro removido com sucesso!")
        elif opcao_livros == 3: #VISUALIZAR LIVROS
            limpar_tela()
            print(Livro.visualizar_livros())
            print("\n")
            input("Pressione ENTER para encerrar a visualização ")
        elif opcao_livros == 4: #ATUALIZAR LIVROS
            limpar_tela()
            print(Livro.visualizar_livros())
            id_livro = int(input("Digite o ID do livro que deseja atualizar: "))
            titulo_livro = input("Digite o título nome do livro: ")
            autor_livro = input("Digite o novo autor do livro: ")
            data_livro = input("Digite o novo ano de lançamento do livro: ")
            Livro.atualizar_livro(id_livro, titulo_livro, autor_livro, data_livro)
            print("Livro atualizado com sucesso!")
        elif opcao_livros == 5:
            break
        else:
            limpar_tela()
            print("Digite uma opção válida")

def abrir_menu_emprestimos():
    while True:
        print("\n--- Menu de empréstimos ---")
        print("1. Adicionar empréstimo")
        print("2. Devolução de empréstimo")
        print("3. Visualizar empréstimos")
        print("4. Atualizar empréstimo")
        print("5. Voltar")
        opcao_emprestimo = int(input("Digite a opção desejada: "))
        if opcao_emprestimo == 1:
            Livro.visualizar_livros()
            livro_emprestado = input("Digite o ID do livro emprestado: ")
            usuario_emprestimo = input("Digite o ID do usuário que pegou o empréstimo: ")
            Emprestimo.criar_emprestimo(livro_emprestado, usuario_emprestimo)
        elif opcao_emprestimo == 2:
            id_emprestimo = int(input("Digite o ID do empréstimo que deseja encerrar: "))
            #emprestimo.remover_emprestimo
            print("Empréstimo removido com sucesso!")
        elif opcao_emprestimo == 3:
            print("")
            input("Pressione ENTER para encerrar a visualização")
            #emprestimo.visualizar_emprestimos
        elif opcao_emprestimo == 4:
            id_emprestimo = input("Digite o ID do empréstimo que deseja atualizar: ")
            livro_emprestado = input("Digite o novo livro emprestado: ")
            usuario_emprestimo = input("Digite o novo usuário do empréstimo: ")
            data_devolucao = input("Digite a nova data de devolução do empréstimo: ")
            #emprestimo.atualizar_emprestimo
            print("Empréstimo atualizado com sucesso!")
        elif opcao_emprestimo == 5:
            break
        else:
            print("Digite uma opção válida")

def abrir_menu_usuarios():
    while True:
        print("\n--- Menu de usuários ---")
        print("1. Adicionar usuário")
        print("2. Remover usuário")
        print("3. Visualizar usuários")
        print("4. Atualizar usuário")
        print("5. Voltar")
        opcao_usuario = int(input("Digite a opção desejada: "))
        if opcao_usuario == 1:
            nome_usuario = input("Digite o nome do usuário: ")
            email_usuario = input("Digite o email do usuário: ")
            telefone_usuario = input("Digite o telefone do usuário: ")
            Usuario.cadastrar_usuario(nome_usuario, email_usuario, telefone_usuario)
            print("Usuário cadastrado com sucesso!")
        elif opcao_usuario == 2:
            id_usuario = int(input("Digite o ID do usuario que deseja remover: "))
            #usuario.remover_usuario
            print("Usuário removido com sucesso!")
        elif opcao_usuario == 3:
            print("")
            input("Pressione ENTER para encerrar a visualização")
            #usuario.visualizar_usuarios
        elif opcao_usuario == 4:
            id_usuario = input("Digite o ID do usuário que deseja atualizar: ")
            nome_usuario = input("Digite o novo nome do usuário: ")
            email_usuario = input("Digite o novo email do usuário: ")
            telefone_usuario = input("Digite o novo telefone do usuário: ")
            #usuario.atualizar_usuario
            print("Usuário atualizado com sucesso!")
        elif opcao_usuario == 5:
            break
        else:
            print("Digite uma opção válida")