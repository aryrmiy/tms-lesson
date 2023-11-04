def get_most_frequent_word(text):
    words = text.lower().split()
    word_counts = {}
    most_frequent_word = None
    max_count = 0

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

        if word_counts[word] > max_count:
            max_count = word_counts[word]
            most_frequent_word = word

    return most_frequent_word

text = "i saw you today and saw her "
most_frequent = get_most_frequent_word(text)
print(text, "->", most_frequent)