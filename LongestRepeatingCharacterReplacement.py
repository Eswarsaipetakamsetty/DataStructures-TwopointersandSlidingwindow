def longestRepeatingCharacterReplacement(s, k):
    left = right = maxlen = maxfreq = 0
    hset = [0]*26

    while right < len(s):
        hset[ord(s[right]) - ord('A')]+=1
        maxfreq = max(maxfreq, hset[ord(s[right]) - ord('A')])
        if (((right - left + 1) - maxfreq) > k):
            hset[ord(s[left]) - ord('A')] -= 1
            left += 1
        if ((right - left + 1) - maxfreq) <= k:
            maxlen = max(maxlen, right- left+ 1)
        right+=1
    return maxlen