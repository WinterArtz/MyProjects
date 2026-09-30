# TIC-TAC-TOE

# This might be unoptimized a bit.
# Before you start, please import 'art' module:
"""
    > WINDOWS:
        Press Win+R, type 'cmd', press Enter, type 'pip install art', press Enter, wait for the download to finish, run the project.
    > MAC:
        Press Cmd+Space, type 'Terminal', press Enter, type 'pip install art', press Enter, wait for the download to finish, run the project.
"""
# Enjoy

import time
import random
from art import tprint
a = "1"
b = "2"
c = "3"
d = "4"
e = "5"
f = "6"
g = "7"
h = "8"
i = "9"
all_v = [1, 2, 3, 4, 5, 6, 7, 8, 9]
forbidden = set()
game_status = 1
win = ""

def printgrid():
    global a, b, c, d, e, f, g, h, i
    print()
    print(a, "|", b, "|", c)
    print("__________")
    print()
    print(d, "|", e, "|", f)
    print("__________")
    print()
    print(g, "|", h, "|", i)
    print()

def move_robot():
    global a, b, c, d, e, f, g, h, i
    allowed = [v for v in all_v if v not in forbidden]
    pos = random.choice(allowed)
    if pos == 1:
        a = "O"
    elif pos == 2:
        b = "O"
    elif pos == 3:
        c = "O"
    elif pos == 4:
        d = "O"
    elif pos == 5:
        e = "O"
    elif pos == 6:
        f = "O"
    elif pos == 7:
        g = "O"
    elif pos == 8:
        h = "O"
    else:
        i = "O"
    time.sleep(1)
    print("Wait, the robot is thinking...")
    time.sleep(random.uniform(2.00, 4.00))
    printgrid()
    print(f'The robot placed a zero on square {pos}.')

def check():
    global game_status, a, b, c, d, e, f, g, h, i, win
    n = "X"
    if all(cell == n for cell in [a, b, c]) or all(cell == n for cell in [d, e, f]) or all(cell == n for cell in [g, h, i]) or all(cell == n for cell in [a, d, g]) or all(cell == n for cell in [b, e, h]) or all(cell == n for cell in [c, f, i]) or all(cell == n for cell in [a, e, i]) or all(cell == n for cell in [c, e, g]):
        win = n
        game_status = 0
    n = "O"
    if all(cell == n for cell in [a, b, c]) or all(cell == n for cell in [d, e, f]) or all(cell == n for cell in [g, h, i]) or all(cell == n for cell in [a, d, g]) or all(cell == n for cell in [b, e, h]) or all(cell == n for cell in [c, f, i]) or all(cell == n for cell in [a, e, i]) or all(cell == n for cell in [c, e, g]):
        win = n
        game_status = 0

def move_human():
    global a, b, c, d, e, f, g, h, i
    while True:
        try:
            sq = int(input("Enter the square where you want to place your X: "))
            if sq < 10 and sq > 0:
                if sq == 1:
                    if a == "1":
                        a = "X"
                        forbidden.add(1)
                    else:
                        print(f'Incorrect! There is already a "{a}" in the square 1!')
                elif sq == 2:
                    if b == "2":
                        b = "X"
                        forbidden.add(2)
                    else:
                        print(f'Incorrect! There is already a "{b}" in the square 2!')
                elif sq == 3:
                    if c == "3":
                        c = "X"
                        forbidden.add(3)
                    else:
                        print(f'Incorrect! There is already a "{c}" in the square 3!')
                elif sq == 4:
                    if d == "4":
                        d = "X"
                        forbidden.add(4)
                    else:
                        print(f'Incorrect! There is already a "{d}" in the square 4!')
                elif sq == 5:
                    if e == "5":
                        e = "X"
                        forbidden.add(5)
                    else:
                        print(f'Incorrect! There is already a "{e}" in the square 5!')
                elif sq == 6:
                    if f == "6":
                        f = "X"
                        forbidden.add(6)
                    else:
                        print(f'Incorrect! There is already a "{f}" in the square 6!')
                elif sq == 7:
                    if g == "7":
                        g = "X"
                        forbidden.add(7)
                    else:
                        print(f'Incorrect! There is already a "{g}" in the square 7!')
                elif sq == 8:
                    if h == "8":
                        h = "X"
                        forbidden.add(8)
                    else:
                        print(f'Incorrect! There is already a "{h}" in the square 8!')
                else:
                    if i == "9":
                        i = "X"
                        forbidden.add(9)
                    else:
                        print(f'Incorrect! There is already a "{i}" in the square 9!')
                break
            else:
                print("Incorrect number! From 1 to 9 only!")
        except ValueError:
            print("This is not a number! Only numbers from 1 to 9.")
    printgrid()
    print(f'You placed a cross on square {sq}.')

tprint("TIC-TAC-TOE") 
print("Let's play tic-tac-toe!")
print("You are fighting againist the robot!")
print()
time.sleep(1)
while True:
    try:
        player_type = int(input("Type 1 to be first, and type 2 to be second! "))
        if player_type in (1, 2):
            break
        else:
            print("Error! Please enter 1 or 2.")
    except ValueError:
            print("Error! Please enter 1 or 2.")

time.sleep(1.5)

if player_type == 1:
    print("You’re playing as the Xs! You are the first.")
    printgrid()
    move_human()
    next_robot = True
else:
    print("You’re playing as the Xs! You are the second!")
    printgrid()
    move_robot()
    next_robot = False
if next_robot:
    for y in range(8):
        if game_status == 1:
            if y%2 == 0:
                move_robot()
                check()
            else:
                move_human()
                check()
        else:
            break
else:
    for y in range(8):
        if game_status == 1:
            if y%2 != 0:
                move_robot()
                check()
            else:
                move_human()
                check()
        else:
            break
print()
if game_status == 0:
    if win == "X":
        print("You win! Restart the program to play again.")
    else:        
        print("Robot win! Restart the program to play again.")
else:
    print("Draw! Restart the program to play again.")
