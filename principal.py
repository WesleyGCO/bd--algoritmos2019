import sqlite3
import usuario
# import romaneio
import cliente
import peca
import getpass from getpass


# usuario.criar_tab_usuario(conexao)
# peca.criar_tab_peca(conexao)
## romaneio.criar_tab_romaneio()
# cliente.criar_tab_cliente(conexao)

# =======================================================

def conferir_usuario(conexao):
    usuario.listar_usuario(conexao)
    cursor = conexao.cursor()

    log = input("Login: ")
    sen = getpass("Senha: ")

    sql = """ 
        SELECT rowid, * FROM usuario;
        """

    cursor.execute(sql)

    listaconf = cursor.fetchall()

    for c in listaconf:
        while(True):

            if (log == c[2] and sen == c[3]):
                print("""
                ==== MENU PRINCIPAL ==== \t\t
                
                1. Registrar peça
                2. Registrar cliente
                3. Gerar romaneio
                4. Relatório de peças
                5. Relatório de cadastro de clientes
                6. Relatório de romaneios
                7. Sair
                """)

                opcao = int(input("Digite a opção escolhida: "))
                while(True):
                    if (opcao == 1):
                        peca.inserir_peca(conexao)
                    elif (opcao == 2):
                        cliente.inserir_cliente(conexao)
                    elif (opcao == 3):
                        #     # romaneio.
                    elif (opcao == 4):
                        relatar 
                    elif (opcao == 5):
                        relatar
                    elif (opcao == 6):
                        relatar
                    elif (opcao == 7):
                        print("Você selecionou a opção de sair, até a próxima!")
                        break
                    else:
                        print("Opção inválida!")
            elif (log != c[2] or sen != c[3]):
                print("Login ou senha inválida, deseja continuar (S/N)?: ")
                


conexao = sqlite3.connect("banco.sqlite3")


conferir_usuario(conexao)


conexao.close()
