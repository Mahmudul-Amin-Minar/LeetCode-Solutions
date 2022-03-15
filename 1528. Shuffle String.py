def restoreString(self, s: str, indices) -> str:
    s_arr = [""]*len(indices)
    
    for i in range(len(indices)):
        s_arr[indices[i]] = s[i]
    return "".join(s_arr)