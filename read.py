import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='07072022',
    database='dbcrud',
)

cursor = conexao.cursor()

def read():
    comando = f'SELECT * FROM cadastro'
    cursor.execute(comando)
    resultado = cursor.fetchall() #lendo banco de dados
    print(resultado)
    cursor.close()
    conexao.close()



read()
