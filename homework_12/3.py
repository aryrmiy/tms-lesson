import re


def is_float_number(string: str) -> bool:
    return re.fullmatch(r'\d+\.\d+', string) is not None


assert is_float_number('24.89')
assert is_float_number('795.3528')
assert not is_float_number('3162')
assert not is_float_number('23-92')