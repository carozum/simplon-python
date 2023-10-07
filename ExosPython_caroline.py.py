"""Exercice 1 : les impairs
Écrire une fonction qui prend 2 nombres en paramètres, et qui affiche, dans l'ordre croissant, tous les entiers impairs se trouvant entre ces deux nombres. Vous devez afficher ces nombres, en les séparant uniquement d'un espace.
Exemple : fonction(42.75, 52.23) doit renvoyer 43 45 47 49 51"""
from math import floor
from random import randint


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


"""
Exercice 2 : le jeu du plus ou moins
"""


# ****** Function that check if a number input by user meets the requirements
def check_input(num, tries):
    while True:
        try:
            num = int(num)
            if num > 100 or num < 0:
                raise ValueError(
                    "\nThe number must be between 0 and 100. \nTry again. ")
        except ValueError as err:
            if 'base 10' in str(err):
                num = input(
                    "\nPlease be sure to enter a number. \nTry again:  ")
            else:
                num = input(err)
        else:
            tries += 1
            return num, tries


# ****************** function that displays the stats for all the games
def display_stats(games):
    average = sum(games) / len(games)
    games.sort()
    min = games[0]
    max = games[len(games)-1]
    return (f"""
        \nAverage tries: {average}
        \rMin number of tries: {min}
        \rMax number of tries {max}""")


# ************** function that plays a game
def guess_num(games):
    guess = randint(1, 100)
    print(guess)

    num = input("\nEnter a number between 0 and 100: ")
    num, tries = check_input(num, 0)

    still_playing = True

    while still_playing:
        if num > guess:
            num = input("\nToo high.\nTry again: ")
            num, tries = check_input(num, tries)

        elif num < guess:
            num = input("\nToo low. \nTry again: ")
            num, tries = check_input(num, tries)
        else:
            games.append(tries)
            print(f"""
        \nGREAT!!! You have guess the number {guess} after {tries} tries
        \r {display_stats(games)}
        \n*****************************""")
            want_to_play = input("\nDo you want to play again ? Y/N ")
            if want_to_play.upper() != "Y":
                return "See you next time"
            else:
                guess_num(games)


def main():
    print(
        f"""*****************************
    \n
    \rEXERCICE 2 - Guessing game
    \rChoose your difficulty level : 
    \r - Choose A to guess a number between 0 and 10
    \r - Choose B to guess a number between 0 and 50
    \r - Choose C to guess a number between 0 an 100
    """)
    games = []
    print(guess_num(games))


if __name__ == "__main__":
    main()
