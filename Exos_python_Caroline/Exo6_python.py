print(
    f"""*****************************
    \nEXERCICE 6 - Tableau de pascal
    \r
    \r*****************************""")


def pascal(n):

    pascal_d = {1: [1, 1]}

    for i in range(2, n+1):
        list_p = []
        list_p.append(1)
        for j in range(1, i):
            list_p.append(pascal_d[i-1][j-1] + pascal_d[i-1][j])
        list_p.append(1)
        pascal_d[i] = list_p
    return pascal_d[n]


n = int(input("choisir un nombre entier: "))
print(
    f"La suite de pascal de rang {n} est {pascal(n)} et son max est {max(pascal(n))}\n")


# pascal = {1: [1, 1]}
# # niveau 2
# list_p = []
# list_p.append(1)
# list_p.append(pascal[1][0] + pascal[1][1])
# list_p.append(1)
# pascal[2] = list_p
# print(pascal)
# # niveau 3
# list_p = []
# list_p.append(1)
# list_p.append(pascal[2][0] + pascal[2][1])
# list_p.append(pascal[2][1] + pascal[2][2])
# list_p.append(1)
# pascal[3] = list_p
# print(pascal)

# # niveau 4
# list_p = []
# list_p.append(1)
# list_p.append(pascal[3][0] + pascal[3][1])
# list_p.append(pascal[3][1] + pascal[3][2])
# list_p.append(pascal[3][2] + pascal[3][3])
# list_p.append(1)
# pascal[4] = list_p
# print(pascal)


# pascal(1)
# pascal(2)
# pascal(3)
