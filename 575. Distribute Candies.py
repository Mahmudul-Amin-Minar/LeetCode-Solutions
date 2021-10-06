def distributeCandies(candyType) -> int:
        half = len(candyType)//2
        candyType = set(candyType)
        print(half, len(candyType))
        if half <= len(candyType):
            return half
        else:
            return len(candyType)

print(distributeCandies([1,1,2,3]))