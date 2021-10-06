def fizzBuzz(n: int):
    str_array = []
    for i in range(1, n+1):
        if(i%3 == 0 and i%5 == 0):
            str_array.append('FizzBuzz')
        elif(i%3 == 0):
            str_array.append('Fizz')
        elif(i%5 == 0):
            str_array.append('Buzz')
        else:
            str_array.append(str(i))
    return str_array

print(fizzBuzz(19))