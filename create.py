import mysql.connector
import getpass

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='07072022',
    database='dbcrud',
)

cursor = conexao.cursor()

def create():
    #creat
    cursor = conexao.cursor()
    nome = str(input("Digite seu nome: "))
    email = str(input("Digite seu email: "))
    telefone = str(input("Digite seu numero de telefone: "))

    comando = f'INSERT INTO cadastro (nome,email,telefone) VALUES ("{nome}", "{email}", "{telefone}")'
    cursor.execute(comando)
    conexao.commit() #edita o banco de dados
    resultado = cursor.fetchall() #lendo banco de dados

    cursor.close()
    conexao.close()


create()
