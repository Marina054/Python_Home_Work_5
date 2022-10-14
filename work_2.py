# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

# count_candies = int(input('Введите количество конфет: '))
# first_player, second_player = input('Введите имя первого игрока: '), input('Введите имя второго игрока: ')
# start = first_player
# while count_candies >0:
#     print('Количество оставшихся конфет: {}'.format(count_candies))
#     while True:
#         delete = int(input('Ход игрока {}(1-28):'.format(start)))
#         if delete >= 1 and delete <= 28:
#             break
#     count_candies -= delete    
#     start = second_player if start == first_player else first_player

# print('Победил {}' . format(start))

import random
def start():
    print(f'Всего 2021 конфета')
    print(f'Игроки по очереи берут конфеты от 1 до 28')
    print(f'Кто заберет последние, тот ВЫЙГРАЛ!!!')
    print(f'Игра началась!)))))')

def rnd_turn():
    print(f'Кто будет ходить первым?:')
    print(f'введите 0, если первый Вы')
    print(f'Нажмите 1 если первым будет компьютер')
    while True:
        n = input('> ')
        if n.isdigit():
            n = int(n)
            if n > 1 or n < 0:
                print(f'введите 0 или 1')
            else: 
                if n == 0:
                    print(f' Первым будет ходить игрок!')
                    break
                else:
                    print(f'Первым будет ходить компьютер!')
                    break
        else:
            print(f'вы ввели недопустимый символ. Введите 0 или 1')
    return n        

def turn_player(motion):
    n = 29
    while n > 28 or n < 1:
        n = input('сколько вы возьмете конфет?')
        if n.isdigit():
            n = int(n)
            if n > 28 or n < 1:
                print(f'Вы взяли недопустимое количество конфет:')
            if n > motion:
                print (f'вы взяли больше чем осталось конфет')   
                n = 29
        else: 
            print(f'Вы ввели недопустимые символы.Ввведите число от 1 до 28')
    return n

def turn_comp(motion):
    n = motion % 29
    if n == 0:
        n = random.randint(1, 28)
    return n

motion = 200
count = 1
start()
turn = rnd_turn()
while True:
    print(f'\nХод №: {count}')
    if turn % 2 == 0:
        print(f'Ход игрока! Всего конфет:{motion}')
        n = turn_player(motion)
        print(f'Игрок взял конфет: {n}')
    elif turn % 2 == 1:
        print(f'Ход компьютера! Всего конфет:{motion}')
        n = turn_comp(motion)
        print(f'компьютер взял конфет:{n}')
    motion -= n 
    if motion == 0:
        if turn % 2 ==0:
            print(f'Победил игрок!')
        else:
            print(f'Победил компьютер!')
        break
    turn += 1
    count += 1              