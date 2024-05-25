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

def insertionSort2(n, arr):
    # Write your code here
    for i in range(1,n):
        tmp = arr[i]
        index = i
        while arr[index-1] > tmp and index > 0:
            arr[index] = arr[index-1]
            index -=1
        arr[index] = tmp
        print (" ".join([str(a) for a in arr]))
