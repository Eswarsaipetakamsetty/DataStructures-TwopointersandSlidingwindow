def MaxConsecutiveOnes(nums, k):  #O(n^2) better solution
    maxlen = 0
    l = 0
    r = 0
    zeros = 0
    while r < len(nums):
        if nums[r] == 0:
            zeros += 1
        while zeros > k:
            if nums[l] == 0:
                zeros -= 1
            l+=1
        if zeros <= k:
            maxlen = max(maxlen, r-l+1)
        r+=1
    return maxlen

def maxConsecutiveOnes(nums, k):
    l = 0
    r = 0
    maxlen = 0
    length = 0 
    zeros = 0
    while r < len(nums):
        if nums[r] == 0:
            zeros += 1
        if zeros > k:
            if nums[l] == 0:
                zeros -=1
            l += 1
        if zeros <= k:
            maxlen = max(maxlen, r-l+1)
        r+=1
    return maxlen


            