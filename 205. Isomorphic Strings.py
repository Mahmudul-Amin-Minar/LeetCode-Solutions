def isIsomorphic(s: str, t: str):
    mapped = zip(s,t)
    len_first_string = len(set(s))
    len_second_string = len(set(t))
    len_mapped_string = len(set(mapped))

    return len_first_string == len_mapped_string == len_second_string

print(isIsomorphic('add', 'egg'))
