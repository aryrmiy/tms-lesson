my_dict = {'a': 7, 'b': 3, 'c': 5}

max_number = None
key_number = None
for key, value in my_dict.items():
    if max_number is None or value > max_number:
        max_number = value
        key_number = key

print(key_number)