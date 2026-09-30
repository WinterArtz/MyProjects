import random

print('Welcome to random number generator!')
while True:
    try:
        x = int(input('Enter the left number limit: '))
        break
    except ValueError:
        print('This is not an integer!')
while True:
    try:
        y = int(input('Enter the right number limit: '))
        break
    except ValueError:
        print('This is not an integer!')
while True:
    try:
        z = int(input('Enter the step value: '))
        break
    except ValueError:
        print('This is not an integer!')
while True:
    try:
        r = int(input('How many numbers you want? '))
        break
    except ValueError:
        print('This is not an integer!')
for i in range(r):
    num = random.randrange(x, y+1, z)
    print(f"Number {i+1}: {num}")
print('''Restart program to enter new values!''')
