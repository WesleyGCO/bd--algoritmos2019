import sqlite3
import usuario
import romaneio
import cliente
import peca


def conferir_usuario(conexao):
    cursor = conexao.cursor()

    log = input("Login: ")
    sen = input("Senha: ")

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
                2. Gerar romaneio
                3. Registrar cliente
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
                        romaneio.
                    elif (opcao == 3):
                        cliente.inserir_cliente(conexao)
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
