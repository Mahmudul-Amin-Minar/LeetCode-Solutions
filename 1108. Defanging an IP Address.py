def defangIPaddr(address: str) -> str:
    defanged_add = ""
    
    for s in address:
        if s == '.':
            defanged_add += "[.]"
        else:
            defanged_add += s
    return defanged_add