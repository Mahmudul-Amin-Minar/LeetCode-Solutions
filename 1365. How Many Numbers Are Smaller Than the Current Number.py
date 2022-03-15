def smallerNumbersThanCurrent(nums):
    smaller = []
    l = len(nums)
    
    for i in range(l):
        count = 0
        for j in range(l):
            if i != j and nums[i] > nums[j]:
                count += 1
        smaller.append(count)
        
    return smaller