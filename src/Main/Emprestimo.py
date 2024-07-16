import mysql.connector
from Livro import Livro
from datetime import datetime, timedelta

class Emprestimo:
    def __init__(self, id, livro_id, usuario_id, data_devolucao):
        self.id = id
        self.livro_id = livro_id
        self.usuario_id = usuario_id
        self.data_devolucao = data_devolucao

    def criar_emprestimo(livro_id, usuario_id):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='86779791',
            database='biblioteca'
        )
        cursor = conn.cursor()

        sql = "SELECT disponivel FROM livros WHERE id = %s"
        val = (livro_id,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        
        if result is None:
            print("Livro não encontrado.")
            return

        disponivel = result[0]

        if disponivel:
            sql = "INSERT INTO emprestimos (id_livro, id_usuario, data_devolucao) VALUES (%s, %s, %s)"
            data_atual = datetime.now()
            tempo_emprestimo = timedelta(days=14)
            data_devolucao = data_atual + tempo_emprestimo
            val = (livro_id, usuario_id, data_devolucao.strftime('%Y-%m-%d'))
            cursor.execute(sql, val)
            
            sql_update = "UPDATE livros SET disponivel = FALSE WHERE id = %s"
            cursor.execute(sql_update, (livro_id,))

            conn.commit()
            print("Empréstimo concluído com sucesso!")
        else:
            print("Este livro não está disponível para empréstimo.")

        cursor.close()
        conn.close()
    
    def registrar_devolucao(id):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='86779791',
            database='biblioteca'
            )
        cursor = conn.cursor()
        sql = "DELETE FROM emprestimos WHERE id = %s"
        val = (id)
        cursor.execute(sql, val)
        sql_update = "UPDATE livros SET disponivel = %s WHERE "
        conn.commit()
        cursor.close()
        conn.close()