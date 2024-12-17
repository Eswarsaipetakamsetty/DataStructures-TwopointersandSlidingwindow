def SubArrayCount(arr, k):
    def lessthank(arr, k):
        left = right = 0
        ctr = 0
        hmap = {}
        while right < len(arr):
            hmap[arr[right]] += 1
            while len(hmap) > k:
                hmap[arr[left]] -= 1
                if hmap[arr[left]] == 0:
                    hmap.pop(arr[left])
                left += 1
            ctr += right - left + 1
            right += 1
        return ctr
    return lessthank(arr, k) - lessthank(arr, k-1)
                
    