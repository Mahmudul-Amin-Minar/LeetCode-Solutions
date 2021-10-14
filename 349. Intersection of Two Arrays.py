def intersection(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    nums3 = nums1 & nums2
    return list(nums3)

print(intersection([1,2,2,1], [2,2]))

