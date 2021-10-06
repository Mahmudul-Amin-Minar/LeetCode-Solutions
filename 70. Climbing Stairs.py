# using recursion caught TLE
def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climbStairs(n-1) + climbStairs(n-2)

# using Dynamic Programming

def climbStairs(n: int) -> int:
    # storing the values
    stairs = [1,2]

    for i in range(2, n+1):
        stairs.append(stairs[i-1] + stairs[i-2])
    return stairs[n-1]


print(climbStairs(38))