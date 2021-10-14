def intersect(nums1, nums2):
    num3 = []
    if len(nums1) <= len(nums2):
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    num3.append(nums1[i])
                    nums2[j] = -1
                    break
    elif len(nums1) > len(nums2):
        for i in range(len(nums2)):
            for j in range(len(nums1)):
                if nums2[i] == nums1[j]:
                    num3.append(nums2[i])
                    nums1[j] = -1
                    break
    return num3

print(intersect([4,9,5], [9,4,9,8,4]))

