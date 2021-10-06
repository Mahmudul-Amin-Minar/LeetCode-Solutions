def addDigits(num: int) -> int:

    n = str(num)
    l = len(n)
    sum_ = num

    while(l > 1):
        sum_ = sum(int(i) for i in n)
        l = len(str(sum_))
        n = str(sum_)
    return sum_

print(addDigits(10))
