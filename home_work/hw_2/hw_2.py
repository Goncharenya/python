# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# n = int(input('Введите число: '))
# fuctorial = 1
# for i in range(n):
#     i = i + 1
#     fuctorial = i * fuctorial
# print(fuctorial, end=' ')



# 2) Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

# n = int(input('Введите число: '))
# denominator = 2
# while denominator < n != 0: 
#     if n % denominator == 0:
#         print(denominator)
#         break
#     denominator += 1


# Пример:
# Для n = 15: Ответ: 3
# Для n = 35: Ответ: 5



# 3) Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.


# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]

# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]
n = int(input('Введите число: '))
list = [2, 2, 3, 1, 8]

list2 = range(-n, n + 1)
result = 0
print(list2)

#for i in list2:
    


#print(result)



# 4)Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.


# n = int(input('Введите число: '))
# i = 2
# sum = 0
# for i in range(n):
#     if i % 2 == 0:
#         sum = sum + i
# print(sum)

