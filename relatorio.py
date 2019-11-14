import usuario
import romaneio
import cliente
import peca

# =======================================

def relatar_romaneio(conexao, x):
    cursor = conexao.cursor()

    data = input("Informe um período de consulta (EX: 01/01/19 até 31/01/19): ")
    dia = data[0:2]
    mes = data[4:5]
    ano = data[6:10]

    sql = """ 
        SELECT usuario.nome, peca.descricao, peca.quant, cliente.nome, dtvenda
        FROM romaneio 
        INNER JOIN peca
        ON romaneio.idpec = peca.rowid
        INNER JOIN usuario
        ON romaneio.idusu = usuario.rowid
        INNER JOIN cliente
        ON romaneio.idcli = cliente.rowid
        WHERE dtvenda = 
        """
    cursor.execute(sql)

    listarel = cursor.fetchall()
