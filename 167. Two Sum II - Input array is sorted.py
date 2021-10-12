def twoSum(numbers, target):
    i, j = 0, len(numbers) - 1

    while i < j:
        sum_ = numbers[i] + numbers[j]
        if sum_ == target:
            return [i+1, j+1]
        elif sum_ < target:
            i += 1
        else:
            j -= 1

print(twoSum([2,7,11,15], 9))