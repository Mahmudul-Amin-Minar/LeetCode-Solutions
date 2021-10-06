roman_values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def romanToInt(s: str) -> int:
    length = len(s)

    sum = 0
    i = 0
    for _ in range(0, length):
        if i < length-1:
            roman_number = s[i]
            next_roman_number = s[i+1]

            if roman_values.get(roman_number) < roman_values.get(next_roman_number):
                inter_sum = roman_values.get(next_roman_number) - roman_values.get(roman_number)
                sum += inter_sum
                i += 2
            
            else:
                inter_sum = roman_values.get(roman_number)
                
                sum += inter_sum
                i += 1
    if i < length:
        sum += roman_values.get(s[i])
           
    return sum

print(romanToInt("MDM"))
