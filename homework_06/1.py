lst = list(input().split())


def map_to_tuples(x):
    return list(map(lambda i: (i.upper(), i.lower()), x))


print(map_to_tuples(lst))