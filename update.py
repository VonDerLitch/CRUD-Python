import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='07072022',
    database='dbcrud',
)

cursor = conexao.cursor()

def update():
    id = str(input("Selecione o ID do usuário: "))
    newNome = str(input("Novo nome: "))
    newEmail = str(input("Novo email: "))
    newTelefone = str(input("Novo numero: "))

    comando = f'UPDATE cadastro SET nome = "{newNome}",email = "{newEmail}", telefone = "{newTelefone}" WHERE id = "{id}" '
    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()


update()
