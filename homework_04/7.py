n = int(input())
i = 2
while i <= (n) ** (1/2):
    if n % i == 0:
        print('False')
        break
    i += 1
else:
    print('True')