"""Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8"""


def row_sum_odd_numbers(n):
    list_odd = []
    number_of_odds = int(n * (n+1)/2)
    print(number_of_odds)
    for i in range(number_of_odds):
        list_odd.append(2*i+1)
    print(list_odd)
    return sum(list_odd[-n:])


def row_sum_odd_numbers(n):
    number_of_odds = int(n * (n+1)/2)
    sum = 0
    for i in range(n, number_of_odds):
        sum += (2*i+1)
        print(2*i + 1)

    return sum


print(row_sum_odd_numbers(4))
