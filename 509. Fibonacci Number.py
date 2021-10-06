def fib(n: int) -> int:
    # storing the values
    fib = [0,1]

    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

print(fib(4))
