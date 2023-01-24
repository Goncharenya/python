# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.

# text = input("Введите выражение: ")
# text = text.split()

# for i in range(len(text)):
#     if text[i] != "+" and text[i] != "-" and text[i] != "*" and text[i] != "/":
#         text[i] = int(text[i])

# new_text = []

# for i in range(len(text)):
#     if text[i] == "+" or text[i] == "-":
#         new_text.append(text[i-1])
#         new_text.append(new_text[i])
#     elif text[i+1] == "*":
#         new_text.append(text[i-1] * text[i + 1])
#     elif text[i+1] == "/":
#         new_text.append(text[i-1] / text[i + 1])
# *Пример:*

# 2+2 => 4;

# 1+2*3 => 7;

# 1-2*3 => -5;
# Соколов Никитка: **дополнительно работа со скобками**


# text = input("Введите выражение: ")
# text = text.split()

def process_step (lst_in: list):
    if("/" in lst_in) or ("*" in lst_in):
        for i in range(len(lst_in)):
            if lst_in[i] == "/":
                temp = lst_in[i-1] / lst_in[i+1]
                lst_in[i].pop(i-1)
                lst_in[i].pop(i-1)
                lst_in[i].pop(i-1)
                lst_in[i].instrt(i-1, temp)
                break
            elif lst_in[i] == "*":
                temp = lst_in[i-1] * lst_in[i+1]
                lst_in[i].pop(i-1)
                lst_in[i].pop(i-1)
                lst_in[i].pop(i-1)
                lst_in[i].instrt(i-1, temp)
                break
    else:
        for i in range(len(lst_in)):
            if lst_in[i] == "+":
                temp = lst_in[i-1] + lst_in[i+1]
                lst_in[i].pop(i-1)
                lst_in[i].pop(i-1)
                lst_in[i].pop(i-1)
                lst_in[i].instrt(i-1, temp)
                break
            elif lst_in[i] == "-":
                temp = lst_in[i-1] - lst_in[i+1]
                lst_in[i].pop(i-1)
                lst_in[i].pop(i-1)
                lst_in[i].pop(i-1)
                lst_in[i].instrt(i-1, temp)
                break
    return lst_in

def process_func(values: str):
    res_str = ""

    for el in values:
        if el.isdigit():
            res_str += el
        else:
            res_str += f' {el}'
    res_str = res_str.split()

    for i in range(len(res_str)):
        if res_str[i].isdigit():
            res_str[i] = int(res_str[i])

    count = 0
    for i in res_str:
        if type(el) == str:
            count += 1
        
    for _ in range(count):
        res_str = process_step(res_str)
    
    return res_str[0]

print(process_func('2+4/2*3'))





