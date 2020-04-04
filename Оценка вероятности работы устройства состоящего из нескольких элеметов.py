import random
i = 0
result = 0
#v1 = float(input('Введите вероятность для A ')) На случай если вероятности для устройства задаются каждый раз
#v2 = float(input('Введите вероятность для B '))
#v3 = float(input('Введите вероятность для C '))
#v4 = float(input('Введите вероятность для D '))
#v5 = float(input('Введите вероятность для E '))
#v6 = float(input('Введите вероятность для F '))
v1 = 0.8           #на случай если не изменяется
v2 = 0.7
v3 = 0.95
v4 = 0.85
v5 = 0.9
v6 = 0.7
while i < 100:
    a = random.uniform(0, 1)
    b = random.uniform(0, 1)
    c = random.uniform(0, 1)
    d = random.uniform(0, 1)
    e = random.uniform(0, 1)
    f = random.uniform(0, 1)
    #устройство не работает, если не работает один из модулей, 1 модуль а, второй b,c,d, причем модуль отключится при
    #отключении только всех устройств в модуле
    if a<= v1 and (b <= v2 or c <= v3 or d <= v4) and (e <= v5 or f <= v6):
        result += 1
    i+=1

result /=100
print(result)
