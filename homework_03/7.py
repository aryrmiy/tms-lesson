n = int(input('Write number'))
i = 2
while i <= (n) ** (1/2):
    if n % 1 == 0:
       print('False')
       break
    i += 1
else:
    print('True')