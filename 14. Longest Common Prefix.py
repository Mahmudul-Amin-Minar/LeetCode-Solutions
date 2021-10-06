def longestCommonPrefix(strs):
    
    if not strs:
        return ""
    
    shortest_string = min(strs, key=len)
    for index, character in enumerate(shortest_string):
        for other_string in strs:
            if other_string[index] != character:
                return shortest_string[:index]
    return shortest_string
