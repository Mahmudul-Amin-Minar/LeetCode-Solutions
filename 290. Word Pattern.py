def wordPattern(pattern: str, s: str):

    l1 = list(pattern)
    l2 = list(s.split(' '))
    
    print(l1)
    print(l2)

    mapped = zip(l1,l2)

    print(list(mapped))
    
    # len_pattern = len(set(l1))
    # len_string = len(set(l2))
    # len_mapped_string = len(set(mapped))

    # return len_pattern == len_mapped_string == len_string
    
    

print(wordPattern("aba" ,"cat cat cat dog"))