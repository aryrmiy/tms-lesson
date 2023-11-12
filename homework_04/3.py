flag = False
for num in range(0, 101, 1):
    print(num)

    while True:
        answer = input('Should we break?')
        if answer == 'yes':
            flag = True
            break
        elif answer == 'no':
            break
        print("Don't understand you!!!")
    if flag == True:
        break