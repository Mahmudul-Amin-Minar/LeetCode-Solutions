from math import factorial

def generate(numRows: int):
    pascal = []
    for i in range(numRows):
        inner_pas = []
        for j in range(i+1):
            value = factorial(i) // (factorial(j) * factorial(i-j))
            inner_pas.append(value)
        pascal.append(inner_pas)

    return pascal

print(generate(5))