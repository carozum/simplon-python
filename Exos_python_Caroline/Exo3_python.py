"""Exercice 3 : les plus grands nombres
Générer une liste aléatoire de 100 entiers puis en extraire les 10 plus grands. Généraliser votre algorithme en créant une fonction prenant comme paramètres la taille de la liste initiale et le nombre d’entiers à extraire.
Contrainte : ne pas utiliser les fonctions de tri sort() ou sorted(). Vous pouvez toutefois utiliser ces fonctions dans un second temps pour vérifier vos résultats."""

from random import randint

print(
    f"""*****************************
    \nEXERCICE 3 - the biggest numbers
    \r
    \r*****************************""")


# **** function that
def big_num(max, size, extract):
    randoms = [randint(1, max) for loop in range(1, size+1)]
    print(
        f"Here is a list of random numbers between 0 and {max} \n{randoms} ")

    for i in range(size):
        for j in range(i + 1, size):
            if randoms[i] > randoms[j]:
                randoms[i], randoms[j] = randoms[j], randoms[i]
    # print(randoms)
    print(f"\nThe {extract} biggest numbers are {randoms[-extract:]}")


big_num(max=200, size=100, extract=15)
