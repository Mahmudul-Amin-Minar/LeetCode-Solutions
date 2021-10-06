def findDisappearedNumbers(nums):
    size_of_array = len(nums)
    nums = set(nums)
    real_nums = set([x for x in range(1, size_of_array+1)])
    absent_element = list(real_nums ^ nums)

    # for i in range(0, size_of_array):
    #     # print(i, nums[i])
    #     if(nums[i]):
    #         if(i+1 != nums[i]):
    #             absent_element.append(i+1)
    #     else:
    #         absent_element.append(i+1)
    #     # try:
            
    #     # except:
    #     #     absent_element.append(i+1)
    #         # pass
    return absent_element

print(findDisappearedNumbers([1,1]))

