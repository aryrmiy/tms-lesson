class Rational:
    def __init__(self, numerator: int, denominator: int):
        if isinstance(numerator, int) and isinstance(denominator, int):
            self.__numerator = numerator
            self.__denominator = denominator
            self.__normalise()

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__numerator

    def __str__(self):
        return f'{self.__numerator} / {self.__denominator}'

    def __mul__(self, other: 'Rational') -> 'Rational':
        new_numerator = (self.__numerator * other.__numerator)
        new_denominator = (self.__denominator * other.__denominator)
        return Rational(numerator=new_numerator, denominator=new_denominator)

    def __truediv__(self, other: 'Rational') -> 'Rational':
        new_numerator = (self.__numerator * other.__denominator)
        new_denominator = (self.__denominator * other.__numerator)
        return Rational(numerator=new_numerator, denominator=new_denominator)

    def __add__(self, other: 'Rational') -> 'Rational':
        new_numerator = self.__numerator * other.__denominator + self.__denominator * other.__numerator
        new_denominator = self.__denominator * other.__denominator
        return Rational(numerator=new_numerator, denominator=new_denominator)

    def __sub__(self, other: 'Rational') -> 'Rational':
        new_numerator = self.__numerator * other.__denominator - self.__denominator * other.__numerator
        new_denominator = self.__denominator * other.__denominator
        return Rational(numerator=new_numerator, denominator=new_denominator)

    def __eq__(self, other: 'Rational') -> bool:
        num_first = self.__numerator * other.__denominator
        num_second = self.__denominator * other.__numerator
        return num_first == num_second

    def __ne__(self, other: 'Rational') -> bool:
        return not self == other

    def __lt__(self, other: 'Rational') -> bool:
        first_num = self.__numerator * other.__denominator
        second_num = self.__denominator * other.__numerator
        return first_num < second_num

    def __gt__(self, other: 'Rational') -> bool:
        first_num = self.__numerator * other.__denominator
        second_num = self.__denominator * other.__numerator
        return first_num > second_num

    def __le__(self, other: 'Rational') -> bool:
        first_num = self.__numerator * other.__denominator
        second_num = self.__denominator * other.__numerator
        return first_num <= second_num

    def __ge__(self, other: 'Rational') -> bool:
        first_num = self.__numerator * other.__denominator
        second_num = self.__denominator * other.__numerator
        return first_num >= second_num

    def nod(x: int, y: int) -> int:
        for i in range(min(abs(x), abs(y)), 0, -1):
            if x % i == 0 and y % i == 0:
                return i

    def __normalise(self):
        nod: int = Rational.nod(self.__numerator, self.__denominator)
        self.__numerator //= nod
        self.__denominator //= nod

        if self.__denominator < 0:
            self.__numerator = self.__numerator * -1,
            self.__denominator = self.__denominator * -1


if __name__ == '__main__':
    first = Rational(1, 4)
    second = Rational(4, 6)

    assert str(first) == '1 / 4'
    assert first / second == Rational(3, 8)
    assert first * second == Rational(1, 6)
    assert first + second == Rational(11, 12)
    assert second - first == Rational(5, 12)

    assert Rational(20, 5) == Rational(4, 1)
    assert Rational(5, 7) != Rational(1, 9)

    assert Rational(1, 2) < Rational(3, 1)
    assert Rational(2, 9) <= Rational(2, 3)
    assert Rational(3, 5) <= Rational(6, 10)

    assert Rational(4, 4) > Rational(2, 8)
    assert Rational(2, 3) >= Rational(2, 7)
    assert Rational(2, 4) >= Rational(2, 4)

    num1 = Rational(1, 4)
    num2 = Rational(3, 2)
    num4 = Rational(156, 100)
    num3 = Rational(1, 8)
    assert num1 * (num2 + num3) + num4 == Rational(1573, 800)