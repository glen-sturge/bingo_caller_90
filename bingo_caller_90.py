# Bingo caller for 90 ball bingo.
# We started learning about lists today in programming class.
# Got caught up on the .pop() method and thought of ways it could be utilized.
# Author: Glen Sturge       Date: 2022-11-07

# used this code to create the list of numbers.
# new_string = ""
# for i in range(1, 91):
#     new_string += f"{i}, "
# print(new_string)

import random

bingo_90_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45,
                 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
                 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75,
                 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]

called_list = []

while True:
    hold_screen = input("Press Enter For A New Ball Number! 'B' if Bingo is called!").upper()
    if hold_screen == 'B':
        print("We Have A Winner!")
        break
    select = random.randint(0, (len(bingo_90_list) - 1))
    called_number = bingo_90_list.pop(select)
    print(f"Called Number : {called_number}")
    called_list.append(called_number)

    print(called_list[0:10])
    if 10 < len(called_list):
        print(called_list[10:20])
    if 20 < len(called_list):
        print(called_list[20:30])
    if 30 < len(called_list):
        print(called_list[30:40])
    if 40 < len(called_list):
        print(called_list[40:50])
    if 50 < len(called_list):
        print(called_list[50:60])
    if 60 < len(called_list):
        print(called_list[60:70])
    if 70 < len(called_list):
        print(called_list[70:80])
    if 80 < len(called_list):
        print(called_list[80:])

    if len(bingo_90_list) == 0:
        print("Game Over. All Numbers Called! Are The Players Awake?")
        break
