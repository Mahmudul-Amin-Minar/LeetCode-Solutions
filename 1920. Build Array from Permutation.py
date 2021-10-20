def buildArray(nums):
    l = len(nums)
    new_arr = []
    for i in range(l):
        new_arr.append(nums[nums[i]])
    return new_arr

print(buildArray([0,2,1,5,3,4]))
