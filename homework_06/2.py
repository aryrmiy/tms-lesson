lst = list(input().split())


def remove_vowels(let):
    letters = 'aeiou'
    return list(filter(lambda i: i not in letters, let))


print(remove_vowels(lst))
