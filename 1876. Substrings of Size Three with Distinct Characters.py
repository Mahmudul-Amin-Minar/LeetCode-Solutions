def countGoodSubstrings(s: str) -> int:
    l = len(s) - 2
    count = 0
    
    for i in range(l):
        substr = s[i:i+3]
        set_s = set(substr)
        
        if len(substr) == len(set_s):
            count += 1
    return count