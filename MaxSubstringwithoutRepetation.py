
class Solution:
    def longestUniqueSubstr(self, s):
        hmap = dict()
        maxlen = 0
        l = 0
        r = 0
        while r < len(s):
            if s[r] in hmap and hmap[s[r]] >= l:
                print(hmap)
                l = hmap[s[r]] + 1
            hmap[s[r]] = r
            maxlen = max(maxlen, r - l + 1)
            r+=1
            
        return maxlen
                

