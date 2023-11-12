def hello_world():
    print('Hello world!')


def my_sum(n, m):
    return n + m


def simple_compare(n, m):
    return n < m


def compare(n, m):
    if n < m:
        return -1
    elif n > m:
        return 1
    else:
        return 0


def filter_negative_numbers(numbers: list):
    resultt = []
    for num in numbers:
        if num >= 0:
            resultt.append(num)
    return resultt


n = int(input('Введите номер задачи: '))
if n == 1:
    hello_world()
elif n == 2:
    x = int(input('Введите первое число: '))
    y = int(input('Введите второе число: '))
    result = my_sum(x, y)
    print(f'Сумма чисел: {result}')
elif n == 3:
    x = int(input('Введите первое число: '))
    y = int(input('Введите второе число: '))
    result = simple_compare(x, y)
    print(f'Первое число меньше второго? Ответ: {result}')
elif n == 4:
    x = int(input('Введите первое число: '))
    y = int(input('Введите второе число: '))
    result = compare(x, y)
    print(f'Результат сравнения: {result}')
elif n == 5:
    user_input = input('Введите числа, разделённые пробелом: ')
    numbers = []
    for num in user_input.split():
        numbers.append(int(num))
    filtered_numbers = filter_negative_numbers(numbers)
    print(f'Удалили отрицательные числа из вашего списка: {filtered_numbers}')
else:
    print('Задачи с таким номером нет.')