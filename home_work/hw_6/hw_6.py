# 1) Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.
# [1,2,3,4,22,234,24] ----> [22, 24]

# def getNum():
#     lst = list(map(int, input("Введите числа: ").split()))
#     return ' '.join(map(str, filter(lambda i: 9 < abs(i) < 100, lst)))
# print(f'[{getNum()}]')




# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension
# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.

# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]


# lst = [33, "adfasdf", 44, "sdrawe", 45, "a"]

# lst_1 = list(filter(lambda x: type(x) == int, lst))
# lst_2 = list(filter(lambda x: type(x) == str, lst))

# print(f'Int: {lst_1}')
# print(f'Str: {lst_2}')

# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension
# 3) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


# num = input("Введите число: ")

# def getSum(num):
#     return sum(map(int, num.replace('.', '').replace('-', '').replace(',', '')))
# print(f'Summa: {getSum(num)}')

# Пример:
# - 6782 -> 23
# - 0,56 -> 11