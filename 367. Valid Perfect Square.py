import math

def isPerfectSquare(num: int) -> bool:
    if int(num**0.5)**2 == num:
        return True
    else:
        return False

print(isPerfectSquare(14))

