def containsDuplicate(nums) -> bool:
    len_1 = len(nums)
    len_2 = len(set(nums))
    if len_1 == len_2:
        return False
    else:
        return True

print(containsDuplicate([1,2,3,4,1]))