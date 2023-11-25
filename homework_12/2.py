import re


def is_date(string: str) -> bool:
    return re.fullmatch(r'\d{2}-\d{2}-\d{4}', string) is not None


assert is_date('11-07-1116')
assert is_date('36-06-2017')
assert not is_date('253-05-2008')
assert not is_date('35-0о-2007')