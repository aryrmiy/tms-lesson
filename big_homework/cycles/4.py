his_list = [int(i) for i in input().split()]

find_zero = False
for i in this_list:
    if i == 0:
        find_zero = True
        break

if find_zero:
    print('yes')
else:
    print('no')