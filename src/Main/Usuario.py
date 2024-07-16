import mysql.connector

class Usuario:
    def __init__(self, id, nome, email, telefone):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
    
    def cadastrar_usuario(nome, email, telefone):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='86779791',
            database='biblioteca'
            )
        cursor = conn.cursor()
        sql = "INSERT INTO usuarios (nome, email, telefone) VALUES (%s, %s, %s)"
        val = (nome, email, telefone)
        cursor.execute(sql, val)
        conn.commit()
        cursor.close()
        conn.close()