# 1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# lst = list(map(int, input("Введите числа через пробел: ").split()))
# sum = 0
# for i in range(len(lst)):
#     if i % 2 != 0:
#         sum += lst[i]

# print(sum)


# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# list =[]
# lst = list(map(int, input("Введите числа через пробел: ").split()))
# sum = 0

# for i in range(len(lst)):
#     if i >= len(lst) / 2:
#         break

#     print(i)
#     sum = lst[i] * lst[-1-i]
#     list.append(sum)

# print(list)


# 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# lst = [1.1, 1.2, 3.1, 5, 10.01]
# new_lst = [round(i % 1, 2) for i in lst]
# print(lst, "=>", max(new_lst) - min(new_lst))


# list = [1.4, 1.2, 3.1, 5, 10.01]
# min = 1
# max = 0
# for i in list:
#     if (i - int(i)) <= min:
#         min = i - int(i)
#     if (i - int(i)) >= max:
#         max = i - int(i)
# print(max - min)

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# result = ""
# num = int(input("Введите число: "))

# while num != 0:
#     result = str(num % 2) + result
#     num //= 2

# print(result)


# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


# num = int(input("Введите число: "))


# def getFib(num):
#     numFib = []
#     numA = 1
#     numB = 1
#     for i in range(num ):
#         numFib.append(numA)
#         numA, numB = numB, numA + numB
#     numA = 0
#     numB = 1
#     for i in range(num +1):
#         numFib.insert(0, numA)
#         numA, numB = numB, numA - numB
#     return numFib

# numFib = getFib(num)

# print(getFib(num))
