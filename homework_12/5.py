import re


class WordIterable:
    def __init__(self, string: str):
        self.string = re.findall(r'[а-яА-Яa-zA-Z]+', string)
        self.count = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count == len(self.string):
            raise StopIteration()
        return self.string[self.count]


if __name__ == '__main__':
    text = 'Мама. мыла? раму!'

for w in WordIterable(text):
    print(w)