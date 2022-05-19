money = float(input('Введите сумму '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposite=[]
deposite.append(round(float(per_cent.get('ТКБ'))*0.01*money))
deposite.append(round(float(per_cent.get('СКБ'))*0.01*money))
deposite.append(round(float(per_cent.get('ВТБ'))*0.01*money))
deposite.append(round(float(per_cent.get('СБЕР'))*0.01*money))
print(deposite)
print('Максимальная сумма, которую вы можете заработать', max(deposite))



