def minimumSum(num: int) -> int:
    a,b,c,d = sorted(str(num))
    return int(a+c) + int(b+d)

print(minimumSum(1234))