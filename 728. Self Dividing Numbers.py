def selfDividingNumbers(left: int, right: int):
    numbers = []
    for i in range(left, right+1):
            str_num = str(i)
            j = 0
            if '0' not in str_num:
                for c in str_num:
                    if i % int(c) == 0:
                        j += 1
                if j == len(str_num):
                    numbers.append(i)
            else:
                continue
    return numbers

print(selfDividingNumbers(47, 110))

