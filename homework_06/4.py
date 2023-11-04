from functools import reduce

string = input()
symbol = input()

def my_join(met: str, sym: str):
    return reduce(lambda m, n: m + sym + n, met.split())


print(my_join(string, symbol))