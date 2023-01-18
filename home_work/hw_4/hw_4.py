# Задача №1
from math import pi

num = int(input())
stroka = str(pi)
print(float(stroka[0:num+2]))

# Задача №2
num = int(input("Введите число: "))

i = 2
list = []
while i <= num:
    if num%2 == 0:
        list.append(i)
        num //= i
    else:
        i += 1

print(f"Простые множители: {list}")

# Задача №3

list = [int(i) for i in input("Введите числа: ").split()]
result = []
for i in list:
    if list.count(i) == 1:
        result.append(i)
print("Данные встречаются 1 рвз")
print(*result) # * - распаковывает список

# Задача №4

from random import randint

k = int(input("Введите степень: "))
for i in range(k, 0, -1):
    factor = range(1, 100)
    if factor == 1:
        factor = ''
    else:
        if i != 1:
            factor = f'{factor}*x^{i}+'
        else:
            f'{factor}*x +'
    print(factor, end=' ')

print(f'{randint(1, 101)} = 0')

# Задача №5

