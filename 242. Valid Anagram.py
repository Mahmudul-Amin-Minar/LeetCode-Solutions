def isAnagram(s: str, t: str) -> bool:
    l_s = len(s)
    l_t = len(t)
    if l_s == l_t:
        dic_s = {}
        dic_t = {}
        for i in range(l_s):
            if s[i] in dic_s:
                dic_s[s[i]] += 1
            else:
                dic_s[s[i]] = 1

            if t[i] in dic_t:
                dic_t[t[i]] += 1
            else:
                dic_t[t[i]] = 1
        
        if dic_s == dic_t:
            return True
        else:
            return False
    else:
        return False

print(isAnagram('anagram', 'nagaram'))