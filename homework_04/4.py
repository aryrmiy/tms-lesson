import random
n = random.randint(0, 100)
answer = int(input('введите число: '))
while answer != n:
    if answer < n:
        print("не угадал, число меньше загаданного")
        answer = int(input('введите число: '))
    elif answer > n:
        print("не угадал, число больше загаданного")
        answer = int(input('введите число: '))
print("вы угадали!")