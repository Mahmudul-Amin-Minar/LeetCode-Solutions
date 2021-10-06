def judgeCircle(moves: str) -> bool:
    moves_dic = {
        "U": 0,
        "D": 0,
        "L": 0,
        "R": 0
    }

    for c in moves:
        moves_dic[c] += 1

    if(moves_dic["D"] == moves_dic["U"] and moves_dic["L"] == moves_dic['R']):
        return True
    else:
        return False

print(judgeCircle("UD"))