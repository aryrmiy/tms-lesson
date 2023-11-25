def generate_words(string: str):
    for world in string.split():
        yield world


if __name__ == "__main__":
    text = "мама мыла раму"
    for w in generate_words(text):
        print(w)