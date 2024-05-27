def highestValuePalindrome(s, n, k):
    # Write your code here
    l, r = 0, len(s)-1
    count = 0
    s = list(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            count += 1
    
    if count > k:
        return "-1"
    
    while l <= r:
        if l == r:
            if k > 0:
                s[l] = '9'
            break
        if s[l] != s[r]:
            if k >= 2 and s[l] != "9" and s[r] != "9":
                if k-2 >= count -1:
                    s[l] = "9"
                    s[r] = "9"
                    k -= 2
                else:
                    maxv = max(s[l],s[r])
                    s[l] = maxv
                    s[r] = maxv
                    k -= 1
                count -= 1
            else:
                maxv = max(s[l],s[r])
                s[l] = maxv
                s[r] = maxv
                k -= 1
                count -= 1
        elif s[l] == s[r]:
            if k >= 2 and s[l] != "9" and l != r:
                if k-2 >= count :
                    s[l] = "9"
                    s[r] = "9"
                    k -= 2   
        l += 1
        r -= 1
    return ''.join(s)
