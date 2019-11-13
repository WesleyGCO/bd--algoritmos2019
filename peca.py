# Criação da tabela peca
def criar_tab_peca(conexao):
    cursor = conexao.cursor()

    sql = """ 
        CREATE TABLE peca (
            descricao TEXT NOT NULL,
            quant TEXT NOT NULL,
            preco INTEGER NOT NULL
        );"""

    cursor.execute(sql)

# Inserção das informações da peça
def inserir_peca(conexao):
    descricao = input("Descrição da peça: ")
    quant = input("Quantidade: ")
    preco = input("Preço: ")
    
    cursor = conexao.cursor()

    sql = """
        INSERT INTO peca VALUES(
            '{}',
            '{}',
            '{}'
        );""".format(descricao, quant, preco)


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
        Quantidade: {}
        Preço: {}""".format(p[0], p[1], p[2], p[3]))
