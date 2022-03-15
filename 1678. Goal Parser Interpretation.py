def interpret(command: str) -> str:
    rule = {
        "()": "o",
        "(al)": "al",
        "G": "G"
    }
    
    temp = ""
    result = ""
    
    for i in range(len(command)):
        temp += command[i]
        
        if temp in rule:
            result += rule[temp]
            temp = ""
    return result