def merge(nums1, m: int, nums2, n: int):
    while m> 0 and n>0:
        if nums1[m-1] > nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m = m-1
        else:
            nums1[m+n-1] = nums2[n-1]
            n = n-1
    nums1[:n] = nums2[:n]
    print(nums1)
        

merge([2,5,6,0,0,0], 3, [1,2,3], 3)