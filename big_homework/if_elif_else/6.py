a = int(input('number from 1 to 12: '))
if a <= 2 or a == 12:
    print('winter')
elif a >= 3 and a <= 5:
    print('spring')
elif a >= 6 and a <= 8:
    print('summer')
else:
    print('autumn')