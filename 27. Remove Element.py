def removeElement(self, nums, val) -> int:
    total=0
    while(nums.count(val)):
        nums.remove(val)
    return nums

removeElement([3,2,2,2,2,2,2,2,3], 2)

