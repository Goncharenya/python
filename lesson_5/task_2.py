# 2) Написать программу, которая будет удалять все слова в которых есть "абв"

list = [i for i in input().split()]
new_list = []

for i in list:
    if 'абв' not in i:
        new_list.append(i)
    
print(*new_list)