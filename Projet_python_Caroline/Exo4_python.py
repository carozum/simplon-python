

import time
from random import sample

print(
    f"""*****************************
    \nEXERCICE 4 - sort algorithms
    \r
    \r*****************************""")

micro_seconds = 1000000
size = 100
max = 500

# ***** option 1 - without using sort() - with no extra variable
randoms = sample(range(max), size)
start_time_1 = time.time()

for i in range(size):
    for j in range(i + 1, size):
        if randoms[i] > randoms[j]:
            randoms[i], randoms[j] = randoms[j], randoms[i]

duration_1 = round((time.time() - start_time_1) * micro_seconds, 2)
print("List 1 ", randoms)


# ***** option 2 - without using sort() - using extra variable
randoms = sample(range(max), size)
start_time_2 = time.time()

for i in range(size):
    for j in range(i+1, size):
        if randoms[i] > randoms[j]:
            # temporary variable
            temp = randoms[i]
            randoms[i] = randoms[j]
            randoms[j] = temp

duration_2 = round((time.time() - start_time_2) * micro_seconds, 2)

# ****** option 3
randoms = sample(range(max), size)
start_time_3 = time.time()

for i in range(1, size):
    value = randoms[i]
    j = i-1
    while j >= 0:
        if value < randoms[j]:
            randoms[j+1] = randoms[j]
            randoms[j] = value
            j -= 1
        else:
            break

duration_3 = round((time.time() - start_time_3) * micro_seconds, 2)

# ***** using the sort() method
randoms = sample(range(max), size)
start_time_4 = time.time()
randoms.sort()
duration_4 = round((time.time() - start_time_4) * micro_seconds, 2)


# ***** using the sorted() method
randoms = sample(range(max), size)
start_time_5 = time.time()
new_list = sorted(randoms)
duration_5 = round((time.time() - start_time_5) * micro_seconds, 2)


# ****** and the winner is !!
print(f"""The execution time of 
    \n- algorithm 1 is {duration_1} micro seconds - for loop
    \r- algorithm 2 is {duration_2} micro seconds - for loop using extra variable
    \r- algorithm 3 is {duration_3} micro seconds - while loop with extra variable
    \r- algorithm 4 is {duration_4} micro seconds - using sort()
    \r- algorithm 5 is {duration_5} micro seconds - using sorted()
    """)

print("It seems that we should follow Python best practice by not re-inventing the wheel and using a built in function... I understand that sorted() and sort() are using adaptative merge sort methods that are a lot more efficient that iterative methods. That could seem intuitively logical. ")
