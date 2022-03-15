def maximumWealth(accounts) -> int:
    l = len(accounts)
    return max([sum(i) for i in accounts])