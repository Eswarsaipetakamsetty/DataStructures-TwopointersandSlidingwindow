#max sub array with atmost two types of numbers

def totalFruitsI(fruits):  # time complexity almost equal to O(n^2) at worst case , it is a better solution that bruite force approach
    left = 0
    right = 0
    maxlen = 0
    hmap = dict()
    while right < len(fruits):
        if fruits[right] not in hmap:
            hmap[fruits[right]] = 1
        else:
            hmap[fruits[right]] += 1
        
        if len(hmap) > 2:
            while len(hmap) > 2:
                hmap[fruits[left]] -= 1
                if hmap[fruits[left]] == 0:
                    hmap.pop(hmap[fruits[left]])
                l+=1
        if len(hmap) <= 2:
            maxlen = max(maxlen, right - left + 1)
        right += 1
    return maxlen

def totalFruits(fruits):
    left = 0
    right = 0
    maxlen = 0
    hmap = dict()
    while right < len(fruits):
        hmap[fruits[right]] = 1 if fruits[right] not in hmap else hmap[fruits[right]] + 1
        if len(hmap) > 2:
            hmap[fruits[left]] -= 1
            if hmap[fruits[left]] == 0:
                hmap.pop(fruits[left])
            left += 1
        if len(hmap) <= 2:
            maxlen = max(maxlen, right - left + 1)
        right += 1
    return maxlen
