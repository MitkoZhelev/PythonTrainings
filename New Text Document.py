arr = [2, 3, 4, 10, 40]
low = 0
high = len(arr) - 1
mid = 0
x = 10

while low <= high:
    mid = (low + high) // 2

    if arr[mid] < x:
        low = mid + 1
    elif arr[mid] > x:
        low = mid - 1

    else:
        print("%d" % mid)
        break
