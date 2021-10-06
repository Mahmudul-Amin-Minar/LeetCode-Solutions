def missingNumber(nums) -> int:
    # length = len(nums) + 1
    # numbers = (x for x in range(length))

    # nums.sort()

    # for i in range(length):
    #     n = next(numbers)
    #     try:
    #         if n != nums[i]:
    #             return n
    #     except:
    #         return n

            # ===========or============
    n = len(nums)
    return (n*(n+1))//2 - sum(nums)

    

print(missingNumber([0]))