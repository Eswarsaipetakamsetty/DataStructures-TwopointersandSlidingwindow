def longestKSubstr(s, k):
    left = right = maxlen = 0
    hmap = {}
    while right < len(s):
        hmap[s[right]] = 1 if s[right] not in hmap else hmap[s[right]] + 1
        if len(hmap) > k:
            hmap[s[left]] -= 1
            if hmap[s[left]] == 0: hmap.pop(s[left])
            left += 1
        if len(hmap) <= k:
            maxlen = max(maxlen, right-left+1)
        right+=1
    return maxlen
