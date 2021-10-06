
def majorityElement(nums):
    n = len(nums)
    num_set = set(nums)

    for num in num_set:
        counter = nums.count(num)
        if counter >= n/2:
            print(num)

majorityElement([2,2,1,1,1,2,2])