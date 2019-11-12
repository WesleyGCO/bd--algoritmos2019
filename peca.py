def criar_tab_peca(conexao):
    cursor = conexao.cursor()

    sql = """ 
        CREATE TABLE peca (
            descricao TEXT NOT NULL,
            quant TEXT NOT NULL
        );"""

    cursor.execute(sql)


def inserir_peca(conexao):
    descricao = input("Descrição da peça: ")
    quant = input("Quantidade: ")
    
    cursor = conexao.cursor()

    sql = """
        INSERT INTO peca VALUES(
            '{}',
            '{}'
        );""".format(descricao, quant)


    cursor.execute(sql)
    conexao.commit()
    print("Dados inseridos com sucesso!")


def listar_peca(conexao):
    cursor = conexao.cursor()

    sql = """
        SELECT rowid, * FROM peca
        """

    listapeca = cursor.fetchall()

    print("\n\t ===== Listando peças =====")

    for p in listapeca:
        print("""
        ID: {}
        Descrição: {}
        Quantidade: {}""".format(p[0], p[1], p[2]))
