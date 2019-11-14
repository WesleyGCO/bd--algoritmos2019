def criar_tab_usuario(conexao):
    # Cursor é a estrutura de controle que percorre os registros do banco
    cursor = conexao.cursor()

    sql = ''' CREATE TABLE IF NOT EXISTS usuario (
                nome TEXT NOT NULL,
                login TEXT NOT NULL,
                senha TEXT NOT NULL
            );'''

    # Executa
    cursor.execute(sql)


def inserir_usuario(conexao):
    nome = input("Nome: ")
    login = input("Login: ")
    senha = input("Senha: ")

    cursor = conexao.cursor()

    sql = ''' INSERT INTO usuario VALUES(
                '{}',
                '{}',
                '{}'
        );
    '''.format(nome, login, senha)

    # Executa
    cursor.execute(sql)
    conexao.commit()

    print("Dados inseridos com sucesso!")


def listar_usuario(conexao):
    cursor = conexao.cursor()

    sql = """
        SELECT rowid, * FROM usuario;
    """
    cursor.execute(sql)

    listausu = cursor.fetchall()

    print("\n\t ===== Listando usuários =====")

    for u in listausu:
        # O "u" é um vetor e cada coluna/ordem do select é uma coluna
        # SELET rowid, *
        # Neste caso, u[0] é o rowid, u[1] é o nome, u[2] é o login e u[3] é a senha

        print("""
        ID: {}
        Nome: {}
        Usuário: {}""".format(u[0], u[1], u[2]))
        
