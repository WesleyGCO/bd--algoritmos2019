import peca
import usuario
import cliente


# Criação da tabela romaneio
def criar_tab_romaneio(conexao):
    cursor = conexao.cursor()

    sql = """
        CREATE TABLE IF NOT EXISTS romaneio (
           preco_final INTEGER NOT NULL,
           dtvenda DATE NOT NULL,
           idusu INTEGER NOT NULL,
           idcli INTEGER NOT NULL,
           idpec INTEGER NOT NULL,
           FOREIGN KEY (idusu) REFERENCES usuario (rowid),
           FOREIGN KEY (idcli) REFERENCES cliente (rowid),
           FOREIGN KEY (idpec) REFERENCES peca (rowid) 
        );"""
    
    
    cursor.execute(sql)

def criar_romaneio(conexao):
