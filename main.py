'''
Взаимное расположение двух окружностей

from math import sqrt
x1, y1, r1, x2, y2, r2 = map(int, input('Ввод x1, y1, r1, x2, y2, r2 через пробел: ').split())
d = sqrt((x2 - x1)**2 + (y2 - y1)**2)
if d == 0 and r1 == r2:
    print('окружности идентичны')
elif d == 0 and r1 != r2:
    print('один центр но не касаются')
elif d < abs(r1 - r2):
    print('одна внутри другой')
elif d == abs(r1 - r2):
    print('одна внутри другой и касаются в одной точке')
elif abs(r1 - r2) < d < (r1 + r2):
    print('имеют две общие точки')
elif d == (r1 + r2):
    print('касаются снаружи в одной точке')
elif d > (r1 + r2):
    print('лежат отдельно друг от друга')'''


'''Калькулятор налога

money = int(input('Сумма дохода: '))
status = input('Cтатус резидента (да/нет): ')
if money < 100000:
    tax = 0
elif 100000 < money < 500000:
    tax = (money - 100000) * 0.9
elif 500000 < money < 1000000:
    tax = 40000 + (money - 500000) * 0.85
elif 1000000 < money:
    tax = 115000 + (money - 1000000) * 0.8
if status == 'да' and money < 1000000:
    tax = tax * 0.95
print(tax)'''


'''k = 0
while k < 10:
    k+=1
    print(k)

a = 0
while a < 20:
    if a % 2 != 0:
        print(a)
    a+=1

b = 20
while b > 10:
    print(b)
    b-=1

c = 0
while c != 5:
    print('Python')
    c+=1

e = int(input())

k = 0
while e != 0:
    e = e // 10
    k += 1
print(k)'''