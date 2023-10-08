def reverse_seq(n):
    arr = []
    for i in range(1, n+1):
        arr.append(i)
    arr.sort(reverse=True)
    return arr


print(reverse_seq(5))
