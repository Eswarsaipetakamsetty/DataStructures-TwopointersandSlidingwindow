def minWinSun(s, t):
    left = right = ctr = 0
    minlength = float('inf')
    start = -1
    hmap= {}
    for i in t:
        hmap[i] = 1 if i not in  hmap else hmap[i] + 1
    while right < len(s):
        if s[right] in hmap:
            hmap[s[right]] -= 1
            if hmap[s[right]] == 0: ctr += 1
        while ctr == len(hmap):
            if minlength > right - left + 1:
                minlength = right - left + 1
                start = left
            if s[left] in hmap:
                hmap[s[left]] += 1
                if hmap[s[left]] > 0: ctr -= 1
            left += 1
        right += 1
    return "" if start == -1 else s[start:start+minlength]
        