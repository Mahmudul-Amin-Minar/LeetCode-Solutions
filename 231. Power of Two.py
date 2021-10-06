import math
def isPowerOfTwo( n: int) -> bool:
    if n <= 0:
        return False
    twos = math.floor(math.log(n,2))
    if 2 ** twos == n:
        return True
    return False

print(isPowerOfTwo(-1))