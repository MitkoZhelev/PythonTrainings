
arr = [64, 34, 25, 12, 22, 11, 90]

n = len(arr)


for i in range (0,n-1):
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp


for i in range(n):
    print("%d" %arr[i])
