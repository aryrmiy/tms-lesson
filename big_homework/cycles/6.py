my_dict = {'a': 7, 'b': 3, 'c': 5}

max_number = None
for key, value in my_dict.items():
    if max_number is None or value > max_number:
        max_number = value

print(max_number)