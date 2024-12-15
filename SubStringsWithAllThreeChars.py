def countSubStr(s):
    lastseen = [-1]*3
    ctr = 0
    for i in range(len(s)):
        lastseen[ord(s[i]) - ord('a')] = i
        if lastseen[0] != -1 and lastseen[1] != -1 and lastseen[-1] != -1:
            ctr = ctr + (1+min(lastseen))
    return ctr
