def isHappy(n: int) -> bool:
    memory = set()

    while(n != 1):
        str_num = str(n)
        n = sum(int(i)**2 for i in str_num)
        print(n)
        if n in memory:
            return False
        memory.add(n)
    return True

print(isHappy(19))