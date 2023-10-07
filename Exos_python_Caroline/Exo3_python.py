

from random import sample

print(
    f"""*****************************
    \nEXERCICE 3 - the biggest numbers
    \r
    \r*****************************""")


# **** function extracts the {extract} biggest numbers
def big_num(max, size, extract):
    randoms = sample(range(max), size)
    print(
        f"Here is a list of random numbers between 0 and {max} \n\n{randoms} ")

    for i in range(size):
        for j in range(i + 1, size):
            if randoms[i] > randoms[j]:
                randoms[i], randoms[j] = randoms[j], randoms[i]
    # print(randoms)
    print(f"\nThe {extract} biggest numbers are {randoms[-extract:]}")


big_num(max=1000, size=100, extract=10)
