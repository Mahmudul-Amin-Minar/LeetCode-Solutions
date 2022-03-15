def createTargetArray(nums, index):
    arr=[]
    
    for n,i in zip(nums,index): 
        arr.insert(i,n)
    return arr