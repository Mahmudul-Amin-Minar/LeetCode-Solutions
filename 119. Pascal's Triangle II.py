from math import factorial

def generate(numRows: int):
    pascal = []
    
    for j in range(numRows+1):
        value = factorial(numRows) // (factorial(j) * factorial(numRows-j))
        pascal.append(value)

    return pascal

print(generate(0))