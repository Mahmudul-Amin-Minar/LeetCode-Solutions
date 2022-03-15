def reverseOnlyLetters(s: str) -> str:
    n = len(s)
    new_s = []
    j = n-1
    for i in range(n):
        if s[j].isalpha():
            new_s.append(s[j])
        if not s[i].isalpha():
            new_s.append(s[i])
        j -= 1
    return "".join(new_s)

reverseOnlyLetters("M_n_r_")
        