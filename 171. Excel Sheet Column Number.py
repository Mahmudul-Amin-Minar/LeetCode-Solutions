import string

def titleToNumber(columnTitle: str) -> int:
    letters = [l for l in string.ascii_uppercase]
    length = len(columnTitle)
    value = 0
    for c in columnTitle:
        letter = letters.index(c) + 1
        value = value + (letter * (26 ** (length-1)))
        length -= 1
    return value

print(titleToNumber("FXSHRXW"))