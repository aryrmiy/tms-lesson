def generate_natural_cubes(n):
    return [a ** 3 for a in range(1, n + 1)]


print(generate_natural_cubes(7))
print(generate_natural_cubes(4))