# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя
# используйте пробел.Без min и max

stroka = input("Введите строку из чисел через пробел: ").split(" ")
min = int(stroka[0])
max = int(stroka[0])

for i in stroka:
    if int(i) > max:
        max = int(i)
    if int(i) < min:
        min = int(i)

print(min, max)





