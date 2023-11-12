a = int(input('number 1: '))
b = int(input('number 2: '))
c = int(input('number 3: '))
if a >= b:
    if a >= c:
        print(a)
    else:
        print(c)
else:
    if b >= c:
        print(b)
    else:
        print(c)