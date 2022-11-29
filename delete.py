import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='07072022',
    database='dbcrud',
)

cursor = conexao.cursor()
def delete():
    id = str(input('Id do Usuário a ser deletado: '))
    sure = str(input(f'Tem certeza que quer excluir o id {id} sim ou não:'))
    if sure == 'sim':
        comando = f'DELETE FROM cadastro WHERE id = "{id}"'
        cursor.execute(comando)
        conexao.commit()

        cursor.close()
        conexao.close()
    elif sure == 'não':
        cursor.close()
        conexao.close()
    else:
        print('programa não entendeu sua resposta')


delete()