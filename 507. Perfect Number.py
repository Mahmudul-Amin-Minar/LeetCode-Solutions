import math
def checkPerfectNumber(num: int):
    divisors = []
    i = 1
    while i <= math.sqrt(num):  
        if (num % i == 0) : 
            # If divisors are equal, print only one
            if (num / i == i) :
                divisors.append(i)
            else :
                divisors.append(i)
                divisors.append(num//i)
                # print(i , n//i)
        i = i + 1
    if sum(divisors) - num == num:
        return True
    return False
print(checkPerfectNumber(28))