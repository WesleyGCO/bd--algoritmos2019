# Criação da tabela peca
def criar_tab_peca(conexao):
    cursor = conexao.cursor()

    sql = """ 
        CREATE TABLE IF NOT EXISTS peca (
            descricao TEXT NOT NULL,
            quant TEXT NOT NULL,
            preco REAL (9,2) NOT NULL
        );"""

    cursor.execute(sql)


# Inserção das informações da peça
def inserir_peca_nova(conexao):
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


def inserir_peca_existente(conexao):
    cursor = conexao.cursor()

    sql = """
        SELECT rowid, * FROM peca
        """
    cursor.execute(sql)

    listapeca = cursor.fetchall()

    listar_peca(conexao)

    print(" ")
    id = int(input("Digite o ID da peça que deseja atualização?: "))

    for i in listapeca:
        if (id == i[0]):
            print(" ")
            a = int(input("Quantidade a ser atualizada para mais: "))
            atual = int(i[2]) + a

            # Atualização quant peças
            sql = """ UPDATE peca SET quant = {} WHERE rowid = {}
            """.format(atual, id)

            cursor.execute(sql)
            conexao.commit()

            print("Atualização efetuada!")
            print(" ")


def listar_peca(conexao):
    cursor = conexao.cursor()

    sql = """
        SELECT rowid, * FROM peca
        """
    cursor.execute(sql)
    listapeca = cursor.fetchall()

    print("\n\t ===== Listando peças =====")

    for p in listapeca:
        print("""
        ID: {}
        Descrição: {}
        Quantidade: {}
        Preço cada unidade: {}""".format(p[0], p[1], p[2], p[3]))


def escolher_pec(conexao):
    cursor = conexao.cursor()

    sql = """
        SELECT rowid, * FROM peca
        """
    cursor.execute(sql)
    listapeca = cursor.fetchall()

    print("Escolha a peça: ")

    for p in listapeca:
        print("""
        ID: {}
        Descrição: {}
        Preço cada unidade: {}""".format(p[0], p[1], p[3]))
    
    x = int(input("Digite o ID da peça: "))
    return x

