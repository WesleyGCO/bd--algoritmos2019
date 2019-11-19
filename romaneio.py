import peca
import usuario
import cliente
import sqlite3


# Criação da tabela romaneio
def criar_tab_romaneio(conexao):
    cursor = conexao.cursor()

    sql = """
        CREATE TABLE IF NOT EXISTS romaneio (
           dtvenda TEXT NOT NULL,
           quantidade TEXT NOT NULL,
           precofinal REAL (9,2) NOT NULL,
           idusu INTEGER NOT NULL,
           idcli INTEGER NOT NULL,
           idpec INTEGER NOT NULL,
           FOREIGN KEY (idusu) REFERENCES usuario (rowid),
           FOREIGN KEY (idcli) REFERENCES cliente (rowid),
           FOREIGN KEY (idpec) REFERENCES peca (rowid)
        );"""

    cursor.execute(sql)

# =====================================

def gerar_romaneio(conexao):
    cursor = conexao.cursor()

    dtvenda = input("Data da venda: ")
    quantidade = input("Quantidade de peças: ")
    idusu = input("ID do usuário: ")
    print(" ")
    cliente.listar_cliente(conexao)
    print(" ")
    idcli = input("ID do cliente: ")
    print(" ")
    peca.listar_peca(conexao)
    print(" ")
    idpec = input("ID da peça: ")
    precofinal = input("Preço: ")

    
    sql = """ SELECT rowid, * FROM peca    
        """
    cursor.execute(sql)

    lista = cursor.fetchall()

    for l in lista:
        if (idpec == l[0]):
            atual_quan = int(l[2]) - quantidade

            # Atualização quant peças
            sql = """ UPDATE peca SET quant = {} WHERE rowid = {}
            """.format(atual_quan, idpec)
            
            cursor.execute(sql)
            cursor.commit()
            print(" ")

    sql_insercao = """
        INSERT INTO romaneio VALUES (
            '{}',
            '{}',
            '{}',
            '{}',
            '{}',
            '{}'
        );""".format(dtvenda, quantidade, precofinal, idusu, idcli, idpec)

    cursor.execute(sql_insercao)
    conexao.commit()
    
    print("Romaneio criado com sucesso!")
    
