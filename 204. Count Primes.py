import math

def countPrimes(n: int) -> int:
    if n < 3:
        return 0
    primes = [1] * n
    primes[0] = primes[1] = 0
    
    # primes using seive method
    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i]:
            primes[i*i : n : i] = [0] * len(primes[i*i : n : i])
    return sum(primes)


print(countPrimes(1500000))