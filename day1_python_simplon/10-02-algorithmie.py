import math

"""
Exercices de pseudo code / algorithmie

"""

# ********* 1. Ecrire un algorithme qui affiche tous les numéros de 1 à 9
for loop in range(1, 10):
    print(loop)
print("\n*******************\n")


# ********* 2. Ecrire un algorithme qui échange la valeur de 2 variables
"""
alphabet = « abcdefghijklmnopqrstuvwxyz »
i =26
tant que i différent de 0 :
	affichet i-ème élément de alphabet
	i = i -1
"""


def swap(a, b):
    a, b = b, a
    return [a, b]


print(swap(12, 3))
print("\n*******************\n")


# ****** 3. Ecrire un algorithme qui affiche l'alphabet à l'envers
""" 
alphabet = « abcdefghijklmnopqrstuvwxyz »
i =26
tant que i différent de 0 :
	affichet i-ème élément de alphabet
	i = i -1
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"
count = 26
while count > 0:
    print(alphabet[count-1])
    count -= 1
print("\n*******************\n")

for letter in alphabet[::-1]:
    print(letter)

for letter in reversed(alphabet):
    print(letter)


# ****** 4. Ecrire un algorithme permettant d'épeler un mot en affichant chaque lettre les unes après les autres

""" 
mot= « salut »
pour i de 1 à la longueur de mot :
	afficher i-ème élément de mot
"""

word = input("Which word do you want to spell ? ")
for letter in word:
    print(letter)
print("\n*******************\n")


# ***** 5. Ecrire un algorithme qui affiche les différentes lettres nécessaires pour écrire un mot et le nombre de fois
""" 
mot = "hello"
pour i de 1 à longueur de mot:
    count = 1
    pour j de i+1 à longueur de mot:
        si la lettre à la position i est égale à la lettre à la position j
            ajouter 1 au compteur
    imprimer la lettre et le compteur
"""

new_word = "carolinefaure"

for i in range(len(new_word)):
    count = 1
    for j in range(i+1, len(new_word)):
        if new_word[i] == new_word[j]:
            count += 1
    print(new_word[i], count)


""" 
TODO à coder
lettres = liste vide
occurences = liste vide
pour i de 1 à taille du mot:
    Si ième lettre est dans lettre:
        position = ième lettre dans la liste
        occurences[position] += 1
    Sinon :
        ajouter la Ième lettre du mot dans lettres
        ajouter 1 à la dernière position de occurences

"""
new_word = "carolinefaure"


def nb_lettre(new_word):
    new_word.lower()
    my_dict = {}
    for char in new_word:
        if char in alphabet:
            if char in my_dict.keys():
                my_dict[char] += 1
            else:
                my_dict[char] = 1
    return my_dict


def nb_lettre(new_word):
    new_word.lower()
    my_dict = {}
    for char in new_word:
        if char in alphabet:
            if char in my_dict.keys():
                pass
            else:
                my_dict[char] = new_word.count(char)
    return my_dict


# ************ 6. Écrire un algorithme qui demande un nombre compris entre 10 et 20, jusqu'à ce que la réponse convienne. En cas de réponse supérieure à 20, on fera apparaître un message : “Plus petit !”, et inversement, “Plus grand !” si le nombre est inférieur à 10.
""" 
Demander le nombre
tant que le nombre est supérieur à 20 ou inférieur à 10:
    si le nombre est supérieur à 20:
        imprimer le message plus petit
    si le nombre est inférieur à 10:
        imprimer le message "plus grand!"
    demander une nouvelle valeur pour le nombre
"""


def enter_number(min=10, max=20):
    number = input("Give a number between 10 and 20: ")
    while not number.isDigit():
        number = int(input("Give a number between 10 and 20: "))

    number = eval(number)

    while number > 20 or number < 10:
        if number > 20:
            print("\nToo high")
        elif number < 10:
            print("\ntoo small")
        else:
            print("Bravo")
            number = input("Give a number between 10 and 20: ")


def enter_number(inf=10, sup=20):
    number = input("Give a number between 10 and 20: ")
    while not number.isDigit():
        number = int(input("Give a number between 10 and 20: "))

    number = eval(number)

    if number > 20:
        print("\nToo high")
        enter_number(inf=inf, sup=sup)
    elif number < 10:
        print("\ntoo small")
        enter_number(inf=inf, sup=sup)
    else:
        print("Bravo")


# ******* 7. Écrire un algorithme qui calcule et affiche la surface d’un triangle connaissant sa base et sa hauteur.
""" 
hauteur = 10
base = 20
aire = base * hauteur /2
afficher l'aire
"""
hauteur = 10
base = 20
aire = base * hauteur / 2
print("L'aire vaut: ", aire)


# ******** 8. Écrire un algorithme qui, étant donné le prix unitaire d’un produit (hors TVA), le taux de TVA (en %) et la quantité de produit vendue à un client, calcule et affiche le prix total à payer par ce client.
""" 
prix_unitaire = 200
taux_TVA = 20.6/100
nombre = 30
prix_total = nombre * prix_unitaire * (1 + taux_tva)
afficher prix_total
"""


def total(unit_price, tax_rate, quantity):
    unit_price = 200
    tax_rate = 20.6 / 100
    quantity = 35
    return unit_price * quantity * (1 + tax_rate)


# ******* 9.Écrire un algorithme qui, étant donné les résultats (note entière sur 20) de trois examens passés par un étudiant (exprimés par six nombres, à savoir, la note et la pondération de chaque examen), calcule et affiche la moyenne globale exprimée en pourcentage.
def moyenne(notes, coefs):
    somme_notes = 0
    somme_coef = 0
    for i in range(len(notes)):
        somme_notes += notes[i] * coefs[i]
        somme_coef += coefs[i]
    moyenne_ponderee = somme_notes / somme_coef
    print("La moyenne pondérée est ", moyenne_ponderee)


notes = [17, 12, 9]
coefs = [3, 1, 2]
print(moyenne(notes, coefs))


def moyenne(notes, coefs):
    if len(notes) != len(coefs):
        return "error"
    return sum([n*c for n, c in zip(notes, coefs)]) / sum(coefs)


# ********* 10. Écrire un algorithme qui affiche toutes les combinaisons de deux nombre entre 0 et 99, dans l’ordre croissant au format “00 01, 00 02, 00 03 … 00 99, 01 02, … 97 99, 98 99”. Ne pas oublier les espaces et virgules !
for d1 in range(10):
    for u1 in range(10):
        for d2 in range(10):
            for u2 in range(10):
                if (d1*10 + u1) < (d2*10 + u2):
                    str = f"{d1}{u1} {d2}{u2}"
                    print(str)


combinaisons = ""
for i in range(100):
    if i < 10:
        for j in range(i+1, 100):
            if j < 10:
                combinaisons += f"0{i} 0{j}, "
            else:
                combinaisons += f"0{i} {j}, "
    else:
        for j in range(i+1, 100):
            combinaisons += f"{i} {j}, "
print(combinaisons)


# ******* 11. Écrire un algorithme qui calcule la somme des chiffres d’un nombre entier de 3 chiffres. Réflexion : l’algorithme est-il aussi valide pour les entiers inférieurs à 100 ou supérieur à 1000?

"""nb = 346
c = quotient de la division euclidienne de nb par 100
d = quotient de la division euclidienne de (nb - 100*c) par 10
u = quotient de la division euclidienne de (nb – 100*c - 10*d) par 1
(OU JUSTE u = nb – 100*c - 10*d)
afficher c+d+u"""


def somme_chiffres(nombre):
    nombre_str = str(nombre)
    somme = 0
    for char in nombre_str:
        somme += int(char)
    return somme

# [int(char) for char in str(nombre)]


nombre = 1225
somme_chiffres(nombre)

# manière algorithmique


def somme_chiffres_bis(nombre):

    puissance = 0
    while nombre - 10 ** puissance > 0:
        puissance += 1

    centaine = nombre // 100
    dizaine = (nombre - centaine * 100) // 10
    unite = nombre - centaine * 100 - dizaine * 10
    # print(centaine * 100 + dizaine * 10 + unite)
    return centaine + dizaine + unite


# print(math.log10(nombre))

# TODO a coder !! quel que soit le nombre en entrée 12345 par exemple

# def count(number):
#     # avec le log en base 10
#     print(math.log10(number))
#     # nb_chiffres = log(number)/log(10)
#     centaine = nombre // 100
#     dizaine = (nombre - centaine * 100) // 10
#     unite = nombre - centaine * 100 - dizaine * 10
#     # print(centaine * 100 + dizaine * 10 + unite)
#     # print(centaine + dizaine + unite)


# ******* 12. Écrire un algorithme itératif et un algorithme récursif qui affiche la somme de 1 à n
# itératif
def somme_n(n):
    somme = 0
    for loop in range(n+1):
        somme += loop
    return somme


# récursif
n = int(input("Quel nombre pour la somme réccursive ?"))


def som_r(n):
    if n == 0:
        return 0
    else:
        return som_r(n-1) + n


print("The recursive sum is ", sum)


# ******** 13. Écrire un algorithme itératif et un algorithme récursif qui affiche le produit de 1 à n (ce qu’on appelle la factorielle n et noté n!)

# itératif

def fact_i(n):
    factorielle_i = 1
    for loop in range(1, n+1):
        factorielle_i *= loop
    return factorielle_i


n = int(input("Enter an integer for factorielle_i calculation: "))
fact_i(10)

# récursif


def fact_r(n):
    if n == 0:
        return 1
    else:
        return fact_r(n-1) * n


print(f"factorielle récursive de {n} vaut {fact_r(n)}")

# ******** 14. Écrire un algorithme itératif et un algorithme récursif qui affiche le n-ème terme de la suite de Fibonacci

# itératif


def fibo_i(n):
    fibo = [0, 1]
    for i in range(2, number + 1):
        current_term = fibo[i-2] + fibo[i-1]
        fibo.append(current_term)
    return fibo[number]


number = int(input("Enter an integer to calculate the fibonacci: "))

# récursif


def fibo_r(number):
    fib = [0, 1]
    if number == 0:
        return fib[0]
    elif number == 1:
        return fib[1]
    else:
        return fibo_r[number-2] + fibo_r[number-1]
