# print('Hellow world')
# value = None
# a = 123
# b = 1.23
# value = None

# print(type(b))
# print(b)

# value = 1234
# print(type(value))

# s = 'str'
# print(s, ' - ', a, s)
# print('{} - {} - {}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# list = ['1', 'hellow', 1,]
# print(list)

# print('Введите число a: ')
# a = int(input())

# print('Введите число b: ')
# b = int(input())
# print(a, '+', b, "=", a+b)

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else: 
#     print(b)

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)   

list = [1,2,4,68,23]
for i in list:
    print(i)

list = range(0, 10, 1) # от 0 до 9 каждую 1 цифру
for i in list:
    print(i)