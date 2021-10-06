def isPalindrome(s: str) -> bool:
    reverse_string = s[::-1]

    if s == reverse_string:
        return True

    s_length = len(s)
    if s_length % 2 == 0:
        length = s_length//2
    else:
        length = s_length//2 + 1
    
    count = 0
    j = s_length - 1
    k = j + 1

    for i in range(length):
        if s[i] != s[j]:
            s1 = s[0:i]
            s2 = s[i+1:k]
            s3 = s1+s2
            rev_s3 = s3[::-1]

            s4 = s[0:j]
            s5 = s[j+1:k]
            s6 = s4+s5
            rev_s6 = s6[::-1]

        
            # print(s1, s2, s3, rev_s3)
            # print(s4, s5, s6, rev_s6)

            if s3 == rev_s3 or s6 == rev_s6:
                return True
            else:
                return False
        j -= 1

print(isPalindrome("cbbcc"))