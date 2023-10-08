def count_positives_sum_negatives(arr):

    if arr == []:
        return []

    positive = []
    negative = []
    for i in range(len(arr)):
        if arr[i] > 0:
            positive.append(1)
        if arr[i] < 0:
            negative.append(arr[i])

    return [sum(positive), sum(negative)]


print(count_positives_sum_negatives(
    [0, 0, 0, 0, 0, 0]))
