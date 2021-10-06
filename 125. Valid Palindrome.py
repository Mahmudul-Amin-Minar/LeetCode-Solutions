def isPalindrome(s: str) -> bool:
    string = ''
    for char in s:
        if char.isalnum():
            char = char.lower()
            string += char
            # print(char)
    reverse_string = string[::-1]
    return True if string == reverse_string else False
print(isPalindrome("0P"))