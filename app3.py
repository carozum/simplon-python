def somme_chiffres_bis(nombre):

    puissance = 0
    while nombre - 10 ** puissance > 0:
        puissance += 1
    print(puissance-1)

    sum = 0
    for i in range(puissance-1, -1, -1):
        chiffre = nombre / 10 ** i
        sum += chiffre
        nombre -= chiffre * 10**i
    return sum


somme_chiffres_bis(1345)
