import sqlite3
import usuario
import romaneio
import cliente
import peca
import relatorio
from getpass import getpass
from datetime import datetime


conexao = sqlite3.connect("banco.sqlite3")

usuario.criar_tab_usuario(conexao)
peca.criar_tab_peca(conexao)
romaneio.criar_tab_romaneio(conexao)
cliente.criar_tab_cliente(conexao)

# =======================================================


def exibirMenu():
    print("""
            ==== MENU PRINCIPAL ==== 
                
            1. Registrar peça nova
            2. Adicionar peça existente
            3. Registrar cliente
            4. Gerar romaneio
            5. Relatório de peças
            6. Relatório de cadastro de clientes
            7. Relatório de romaneios
            8. Sair
            """)

# =======================================================


def conferir_usuario(conexao):
    cursor = conexao.cursor()

    print("BEM VINDO AO SISTEMA!")
    print(" ")
    log = input("Login: ")
    sen = getpass("Senha: ")

    now = datetime.now()
    print("Login realizado na data: ", now.day, "/", now.month, "/", now.year, "às", now.hour, "hrs", now.minute, "min", now.second, "sec")
    print(" ")

    sql = """ 
        SELECT rowid, * FROM usuario;
        """

    cursor.execute(sql)

    listaconf = cursor.fetchall()

    for c in listaconf:
            if (log == c[2] and sen == c[3]):
                while(True):
                    exibirMenu()
                    opcao = int(input("Digite a opção escolhida: "))
                    if (opcao == 1):
                        peca.inserir_peca_nova(conexao)
                    elif (opcao == 2):
                        peca.inserir_peca_existente(conexao)
                    elif (opcao == 3):
                        cliente.inserir_cliente(conexao)
                    elif (opcao == 4):
                        romaneio.gerar_romaneio(conexao)
                    elif (opcao == 5):
                        peca.listar_peca(conexao)
                    elif (opcao == 6):
                        cliente.listar_cliente(conexao)
                    elif (opcao == 7):
                        relatorio.relatar_romaneio(conexao)
                    elif (opcao == 8):
                        print("Você selecionou a opção de sair, até a próxima!")
                        break
                    else:
                        print("Opção inválida!")
            else:
                print("Login ou senha inválida, deseja continuar (S/N)?: ")


# usuario.inserir_usuario(conexao)
# usuario.listar_usuario(conexao)
# peca.listar_peca(conexao)


conferir_usuario(conexao)



conexao.close()
