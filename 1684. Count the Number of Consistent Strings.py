def countConsistentStrings(allowed: str, words) -> int:
    allowed = set(allowed)
    
    count = 0
    for word in words:
        for letter in word:
            if letter not in allowed:
                count += 1
                break
    return len(words) - count