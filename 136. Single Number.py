def singleNumber(nums) -> int:
    xor = 0
    for num in nums:
        xor = xor ^ num
    return xor

print(singleNumber([4,1,2,1,2,4,6]))