# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

a, b = int(input("Введите 2 числа: ")), int(input())

if a == b == 0: print (0)
else: 
    for kr in range(max(a,b), a*b + 1):
        if kr% a == 0 and b%2 == 0: break
    print(kr)