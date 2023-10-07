def sum_array(arr):
    if arr == [] or arr == None:
        return 0
    elif len(arr) == 1 or len(arr) == 2:
        return 0
    else:
        arr.sort()
        print(arr)
        print(arr[len(arr)-1])
        sum = 0
        for i in range(1, len(arr)-1):
            sum += arr[i]
        return sum


print(sum_array([6, 2, 1, 8, 10]))
