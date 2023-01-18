# 1) Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.

# 120 21 ---> 99 бот 4 -> 95 .... бот --->29 --> 27 >> 2конф

# a) Добавьте игру против бота

# # Доп b) Подумайте как наделить бота ""интеллектом"" (Теория игр)

# 2) Создайте программу для игры в ""Крестики-нолики"" человек vs человек.

board = [' ', ' ',' ',' ',' ',' ',' ',' ',' ', ] # поле
def print_state(state):
    for i, c in enumerate(state):
        if(i +1) % 3 ==0:
            print(f'{c}')
        else: 
            print(f'{c} |', end = ' ' )

print_state(board)

win_combo = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

def getWinner(state, combo):
    for(x,y,z) in combo:
        if state[x] == state[y] and state[y] == state[z] and (state[x] == 'X' or state[x] == '0'):
            return state[x]
    return ''

def game(board):
    current_step = 'X'
    while (getWinner(board, win_combo) == ''):
        index = int(input(f'Куда тыкнуть {current_step}?'))
        board[index] = current_step

        print_state(board)

        winner = getWinner(board, win_combo)
        if winner != '':
            print(f'Ты победил, {winner}!')
        current_step ='X' if current_step == '0' else '0'

game(board)





# 1 | 2 | X
# 4 | X | O
# X | 8 | O
# 3) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные данные хранятся в отдельных текстовых файлах.
# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"

# Вывод: stroka = "aaabbbbccbbb"