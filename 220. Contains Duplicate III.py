def containsNearbyAlmostDuplicate(nums, k: int, t: int) -> bool:
    if k <= 0 or t < 0:
        return False 
    dic = {}
    for index, value in enumerate(nums):
        d = value//(t+1)
        if d in dic:
            return True
        if d+1 in dic and abs(value - dic[d+1]) <= t:
            return True
        if d-1 in dic and abs(value - dic[d-1]) <= t:
            return True
        dic[d] = value
        if index - k >= 0:
            old_d = nums[index - k]
            del dic[old_d]
    return False

print(containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))