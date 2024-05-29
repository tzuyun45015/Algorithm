def largestPermutation(k, arr):
    # Write your code here
    d = {}
    for i in range(len(arr)):
        d[arr[i]] = i

    i = 0
    while i < n and k > 0:
        if arr[i] < n - i:
            index = d[n-i]
            d[arr[i]] = index
            d[arr[index]] = i
            arr[i], arr[index] = arr[index], arr[i]
            k -= 1
        i += 1
    return arr
