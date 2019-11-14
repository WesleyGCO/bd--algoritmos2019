from datetime import date

data_atual = date.today()
# print(data_atual)
print('{}' "/" '{}' "/" '{}'.format(data_atual.day, data_atual.month, data_atual.year))


data = input("Informe um período de consulta (EX: 01/01/19 até 31/01/19): ")
dia = data[0:2]
mes = data[4:5]
ano = data[6:10]

print(dia, mes, ano)
