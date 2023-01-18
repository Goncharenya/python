# list =[]
# for i in range(1, 21):
#     if i % 2 ==0:
#         list.append(i)
# print(list)

# list = [i for i in range(1, 21)if i % 2 ==0]

# print(list)

# def f(x):
#     return x**3

# list = [(i, f(i)) for i in range(1, 21)if i % 2 ==0] # кортежи
# print(list)

# data = list(map(int,input().split()))
# print(data)
# data = [x for x in range(10)]

# res = list(filter(lambda x: not x%2, data))
# print(res)

users = ['user1', 'user2','user3', 'user4',]
idt = [4, 2, 7, 34]
data = list(zip(users, idt))
print(data)
