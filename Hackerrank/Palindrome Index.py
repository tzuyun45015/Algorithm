def palindromeIndex(s):
    # Write your code here
    l, r = 0, len(s)-1
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            if s[l+1] == s[r] and s[l+2] == s[r-1]:
                return l
            elif s[l] == s[r-1] and s[l+1] == s[r-2]:
                return r
            else: 
                return -1
    return -1
