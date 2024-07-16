import mysql.connector

class Livro:
    def __init__(self, titulo, autor, lancamento):
        self.titulo = titulo
        self.autor = autor
        self.lancamento = lancamento

    def adicionar_livro(titulo, autor, lancamento):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='86779791',
            database='biblioteca'
            )
        cursor = conn.cursor()
        sql = "INSERT INTO livros (titulo, autor, lancamento) VALUES (%s, %s, %s)"
        val = (titulo, autor, lancamento) 
        cursor.execute(sql, val)
        conn.commit()
        cursor.close()
        conn.close()

    def remover_livro(id):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='86779791',
            database='biblioteca'
            )
        cursor = conn.cursor()
        sql = "DELETE FROM livros WHERE id = %s"
        val = (id,)
        cursor.execute(sql, val)
        conn.commit()
        cursor.close()
        conn.close()

    def visualizar_livros():
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='86779791',
            database='biblioteca'
            )
        cursor = conn.cursor()
        sql = "SELECT * FROM livros"
        cursor.execute(sql)
        livros = cursor.fetchall()
        cursor.close()
        conn.close()
        print("Livros cadastrados:")
        for livro in livros:
            print(f"ID do livro: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Lançamento: {livro[3]}")

    def atualizar_livro(id, titulo, autor, lancamento):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='86779791',
            database='biblioteca'
            )
        cursor = conn.cursor()
        sql = "UPDATE livros SET titulo = %s, autor = %s, lancamento = %s WHERE id = %s"
        val = (titulo, autor, lancamento, id)
        cursor.execute(sql, val)
        conn.commit()
        cursor.close()
        conn.close()