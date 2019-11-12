from datetime import date

data_atual = date.today()
# print(data_atual)
print('{}' "/" '{}' "/" '{}'.format(data_atual.day, data_atual.month, data_atual.year))
