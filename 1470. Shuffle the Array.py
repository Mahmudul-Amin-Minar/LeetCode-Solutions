def shuffle(nums, n: int):
    a = nums[0:n]
    b = nums[n:]
    
    i = 0
    j = 0
    while j<n:
        nums[i] = a[j]
        nums[i+1] = b[j]
        i += 2
        j += 1
    return nums