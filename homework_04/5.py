number = int(input('write number '))
summ = 0
while (number != 0):
    summ = summ + number % 10
    number = number // 10
print('', summ)