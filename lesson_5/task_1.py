# list = [int(i) for i in input().split()]

# print(list)

# x^2 x в квадрате
# lst = []
# a = list(map(lambda x: x^2, lst))

# print(list)

# 1) В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 2) Написать программу, которая будет удалять все слова в которых есть "абв"

file = open("lesson_5/text.txt", 'r')

li = [int(i) for i in file.read().split()]

for i in range(1, len(li)):
    if li[i]-1 != li[i-1]:
        print(li[i] -1)




# Ввод:
# привет приаб приабвет
# Вывод:
# привет приаб