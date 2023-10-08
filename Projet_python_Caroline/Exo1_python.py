"""Exercice 1 : les impairs
Écrire une fonction qui prend 2 nombres en paramètres, et qui affiche, dans l'ordre croissant, tous les entiers impairs se trouvant entre ces deux nombres. Vous devez afficher ces nombres, en les séparant uniquement d'un espace.
Exemple : fonction(42.75, 52.23) doit renvoyer 43 45 47 49 51"""
from math import floor


def odds(a, b):
    # ranger les nombres dans le bon ordre
    if a < b:
        num1, num2 = a, b
    else:
        num1, num2 = b, a

    # si num1 est un float l'arrondir au dessus
    if type(num1) == float:
        num1 = floor(num1) + 1

    # si num2 est un float l'arrondi au dessous
    if type(num2) == float:
        num2 = floor(num2)

    # parcourir le range entre num1 et num2
    str_nums = ''
    for num in range(num1, num2+1):
        if num % 2 == 1:
            str_nums += f"{num} "

    return str_nums


a = 42.75
b = 52.23
print(
    f"""*****************************
    \nEXERCICE 1
    \rLa suite de nombres impairs entre {a} et {b} est: 
    \r{odds(42.75, 52.23)}
    \r
    \r*****************************""")
