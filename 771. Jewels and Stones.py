def numJewelsInStones(jewels: str, stones: str) -> int:
    total = 0
    for c in jewels:
        total += stones.count(c)
    return total