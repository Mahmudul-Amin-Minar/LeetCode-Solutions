from sys import maxsize
def maxSubArray(nums) -> int:
    maxSum = -maxsize
    currentSum = 0

    for num in nums:
        currentSum += num
        if currentSum > maxSum:
            maxSum = currentSum
        if currentSum < 0:
            currentSum = 0
    return maxSum

print(maxSubArray([-1000]))
