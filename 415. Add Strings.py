def addStrings(num1: str, num2: str) -> str:
    length = max(len(num1), len(num2))
    num1 = num1.zfill(length)
    num2 = num2.zfill(length)

    result = ''
    carry = 0

    for i in range(length-1, -1, -1):
        x = int(num1[i])
        y = int(num2[i])
        sum_ = carry + x + y

        carry = 0

        if sum_ > 9:
            remainder = sum_%10
            carry = sum_//10

            result = str(remainder) + result
        else:
            result = str(sum_) + result
    if carry != 0:
        result = str(carry) + result

    return result

print(addStrings('1', '9'))



