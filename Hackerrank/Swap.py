def lilysHomework(arr):
    # Write your code here
    arrs=sorted(arr)
    d1={}
    d2={}
    for i in range(len(arr)):
        d1[arr[i]]=arrs[i]
        d2[arr[i]]=arrs[len(arr)-1-i]
    
    return min(swaps(d1),swaps(d2))
    
def swaps(d):
    count = 0
    for x in d.keys():
        y = d[x]
        while(x!=y):
            d[x] = d[y]
            d[y] = y
            y = d[x]
            count += 1 
    return count 
            
