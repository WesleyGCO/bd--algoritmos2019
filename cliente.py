def criar_tab_cliente(conexao):
    cursor = conexao.cursor()

    sql = """
        CREATE TABLE IF NOT EXISTS cliente (
            nome TEXT NOT NULL,
            rg TEXT NOT NULL, 
            cpf TEXT NOT NULL,
            celular TEXT NOT NULL,
            rua TEXT NOT NULL,
            bairro TEXT NOT NULL, 
            num TEXT NOT NULL,
            cidade TEXT NOT NULL,
            estado TEXT NOT NULL
        );"""

    #Executa
    cursor.execute(sql)

def inserir_cliente(conexao):
    nome = input("Nome completo: ")
    rg = input("RG: ")
    cpf = input("CPF: ")
    celular = input("Celular (xx) xxxxx-xxxx: ")
    rua = input("Rua: ")
    bairro = input("Bairro: ")
    num = input("Número: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")

    cursor = conexao.cursor()

    sql = """ INSERT INTO cliente VALUES(
            '{}',
            '{}',
            '{}',
            '{}',
            '{}',
            '{}',
            '{}',
            '{}',
            '{}'
    );""".format(nome, rg, cpf, celular, rua, bairro, num, cidade, estado)

    # Executa
    cursor.execute(sql)
    conexao.commit()
    print("Dados inseridos com sucesso!")


def listar_cliente(conexao):
    cursor = conexao.cursor()

    sql = """ 
        SELECT rowid, * FROM cliente;
    """
    listacli = cursor.fetchall()

    print("\n\t ===== Listando clientes =====")

    for i in listacli:
        print("""
        ID: {}
        Nome: {}
        RG: {}
        Celular: {}""".format(i[0], i[1], i[2], i[4]))


