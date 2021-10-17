def containsNearbyDuplicate(nums, k) -> bool:
    dic = {}
    for index, value in enumerate(nums):
        if value in dic and index - dic[value] <= k:
            return True
        dic[value] = index
    return False

print(containsNearbyDuplicate([1,2,3,1], 2))