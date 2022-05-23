k = int(input("Введите сколько билетов вам нужно: "))
S = 0
for i in range(1, k+1):
    print("Введите возраст ", i, " посетителя: ")
    a = int(input())
    if a >= 25:
        S = S + 1390
    elif 25 > a >= 18:
        S = S + 990
if k >= 4:
    S = S - S*0.1
    print("Cумма к оплате c учетом скидки: ", S)
else:
    print("Сумма к оплате: ", S)

