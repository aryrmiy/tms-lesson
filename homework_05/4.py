def get_longest_word(text):
    words = text.split()
    longest_word = ""

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

text = "this day is rainy but beautiful"
result = get_longest_word(text)
print(text, "->", result)