def commonChars(words):
    check = list(words[0])

    for word in words[1:]:
        newCheck = []
        for c in word:
            if c in check:
                newCheck.append(c)
                check.remove(c)
        check = newCheck
    
    return check

print(commonChars(["cool","lock","cook"]))
