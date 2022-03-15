def spiralOrder(matrix):
    linear_ara = []
    
    m = len(matrix)
    if m == 0:
        return linear_ara
    n = len(matrix[0])
    
    left = 0
    right = n-1
    top = 0
    bottom = m-1
    
    direction = 0
    while top <= bottom and left <= right:
        
        # traverse for left to right
        if direction == 0:
            for i in range(left, right+1):
                linear_ara.append(matrix[top][i])
            top += 1
        
        # traverse for top to bottom
        if direction == 1:
            for i in range(top, bottom+1):
                linear_ara.append(matrix[i][right])
            right -= 1
        
        # traverse for right to left
        if direction == 2:
            for i in range(right, left-1, -1):
                linear_ara.append(matrix[bottom][i])
            bottom -= 1
        
        # traverse for bottom to top
        if direction == 3:
            for i in range(bottom, top-1, -1):
                linear_ara.append(matrix[i][left])
            left += 1
        direction = (direction + 1) % 4
        
    return linear_ara