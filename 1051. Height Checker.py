def heightChecker(heights) -> int:
    expected = heights[:]
    expected.sort()
    
    indices = 0
    for i in range(len(heights)):
        if expected[i] != heights[i]:
            indices += 1
            
    return indices