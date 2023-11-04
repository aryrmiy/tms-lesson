def generate_squares(*args):
    squares = [x ** 2 for x in args]
    return squares


print(generate_squares(1, 2, 3))