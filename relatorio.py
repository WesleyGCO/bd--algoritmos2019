from datetime import datetime

# =======================================


def relatar_romaneio(conexao):
    cursor = conexao.cursor()

    data = input("Informe uma data a ser pesquisada: ")

    sql = """ 
        SELECT usuario.nome, peca.descricao, cliente.nome, quantidade, dtvenda
        FROM romaneio 
        INNER JOIN peca
        ON romaneio.idpec = peca.rowid
        INNER JOIN usuario
        ON romaneio.idusu = usuario.rowid
        INNER JOIN cliente
        ON romaneio.idcli = cliente.rowid
        WHERE dtvenda >= {}
        """.format(data)
    
    cursor.execute(sql)

    listarel = cursor.fetchall()

    for u in listarel:
        if (data >= u[4]):
            now = datetime.now()
            print("Relatório realizado na data: ", now.day, "/", now.month, "/", now.year, "às", now.hour, "hrs", now.minute, "min", now.second, "sec")
            print(" ")

            print("""
            ==== RELATÓRIO DE ROMANEIOS ====

            Usuário: {}
            Descrição da peça: {}
            Cliente: {}
            Quantidade: {}
            Data da venda: {}            
            """.format(u[0], u[1], u[2], u[3], u[4]))
        else:
            print("Nenhum registro nessa data!")
