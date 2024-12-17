from typing import List

def distinctSubKOdds(arr: List[int], k: int) -> int:
    for i in range(len(arr)):
        if arr[i]%2 == 0:
            arr[i] = 0
        else:
            arr[i] = 1
    def atmost(arr, k):
        right = left = s = ctr = 0
        while right < len(arr):
            s += arr[right]
            while s > k:
                s -= arr[left]
                left += 1
            ctr += right - left + 1
            right += 1
        return ctr
    return atmost(arr, k) - atmost(arr, k-1)