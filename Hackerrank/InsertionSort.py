def insertionSort1(n, arr):
    i=n-1
    while i>0:
        if arr[i]<arr[i-1]:
            temp=arr[i]
            arr[i]=arr[i-1]
            print(*arr)
            arr[i-1]=temp
            i=i-1
        else:
            break
    print(*arr)
