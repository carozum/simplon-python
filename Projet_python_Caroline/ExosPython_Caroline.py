
import json
import io
import pickle
from glob import glob
from os.path import isfile
import os
import time
from random import sample
from random import randint
from math import floor


# ************************************************************************
# *********************** EXO 1 ******************************************
# ************************************************************************

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
    \nEXERCICE 1 - impairs
    \rLa suite de nombres impairs entre {a} et {b} est: 
    \r{odds(42.75, 52.23)}
    \r
    \r*****************************""")


# ************************************************************************
# *********************** EXO 2 ******************************************
# ************************************************************************


# ****** Function that check if a number input by user meets the requirements


def check_input(num, tries, sup):
    while True:
        try:
            num = int(num)
            if num > sup or num < 0:
                raise ValueError(
                    f"\nThe number must be between 0 and {sup}. \nTry again. ")
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


# ********* function that asks for the level of game chosen


def ask_level():
    print(
        f"""There are different levels of your difficulty: 
    \r - A to guess a number between 0 and 10
    \r - B to guess a number between 0 and 50
    \r - C to guess a number between 0 an 100
    """)
    level = input('Select your level: ')
    if level.upper() == "A":
        sup = 10
    elif level.upper() == 'B':
        sup = 50
    else:
        sup = 100
    return sup


# ************** function that plays a game
def guess_num(games, sup):

    guess = randint(1, sup)
    # print(guess)

    num = input(f"\nEnter a number between 0 and {sup}: ")
    num, tries = check_input(num, 0, sup)

    still_playing = True

    while still_playing:
        if num > guess:
            num = input("\nToo high.\nTry again: ")
            num, tries = check_input(num, tries, sup)

        elif num < guess:
            num = input("\nToo low. \nTry again: ")
            num, tries = check_input(num, tries, sup)
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
                sup = ask_level()
                guess_num(games, sup)


def main():
    print(
        f"""*****************************
    \n
    \rEXERCICE 2 - Guessing game
    """)
    sup = ask_level()
    games = []
    print(guess_num(games, sup))


main()


# ************************************************************************
# *********************** EXO 3 ******************************************
# ************************************************************************


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


# ************************************************************************
# *********************** EXO 4 ******************************************
# ************************************************************************


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


# ************************************************************************
# *********************** EXO 5 ******************************************
# ************************************************************************

"""
Écrire un programme qui convertit en mètres par seconde et en km/h une vitesse fournie par l'utilisateur en miles/heure (1 mile = 1609 mètres). Afficher le résultat avec uniquement 2 chiffres après la virgule.
"""

print(
    f"""*****************************
    \nEXERCICE 5 - conversion
    \r
    \r*****************************""")


def convert_time(total_seconds):
    one_year = 36525 * 24 * 36
    one_month = 3043.7 * 24 * 36
    one_day = 24 * 3600
    one_hour = 3600
    one_minute = 60

    years = total_seconds // one_year
    years_remainder = total_seconds - years * one_year

    months = years_remainder // one_month
    months_remainder = years_remainder % one_month

    days = months_remainder // one_day
    days_remainder = months_remainder % one_day

    hours = days_remainder // one_hour
    hours_remainder = days_remainder % one_hour

    minutes = hours_remainder // one_minute
    minutes_remainder = hours_remainder % one_minute

    return f"""
        \n{total_seconds} secondes correspondent à :
        \r{years} années {months} mois {days} jours
        \r{hours} heures {minutes} minutes {minutes_remainder} secondes
        """


print("Conversion seconds to year/month/day/hour/minute/seconds")
print(convert_time(3430061596791935255))


def speed_km_h(speed):
    return round(speed * 1609 / 1000, 2)


def speed_m_s(speed):
    return round(speed * 1609 / 3600, 2)


speed = 120
print("***********************")
print("Conversion miles per hour to km per hour")
print(f"\n{speed} mile(s) per hour are about {speed_km_h(speed)} km per hour")

print("\n***********************")
print("Conversion miles per hour to meter per second")
print(f"\n{speed} mile(s) per hour are about {speed_m_s(speed)} meter(s) per hour")
print("\n***********************")


# ************************************************************************
# *********************** EXO 6 ******************************************
# ************************************************************************


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


# ************************************************************************
# *********************** EXO 7 ******************************************
# ************************************************************************

print(
    f"""*****************************
    \nEXERCICE 7 - Manipulation de dictionnaires
    \r
    \r*****************************""")


def exchange_dict(dico):
    exchanged = {}
    for key, value in dico.items():
        exchanged[value] = key
    return exchanged


dico = {"one": "un", "two": "deux"}
print(f"""
      \nThe english/french dictionary is:
      \r{dico}
      \rThe French/English dictonary is 
      \r{exchange_dict(dico)}
      """)


# ************************************************************************
# *********************** EXO 8 ******************************************
# ************************************************************************

# source : https://www.pythontutorial.net/python-basics/python-read-text-file/


print(
    f"""*****************************
    \nEXERCICE 8 - manipulation de fichiers textes
    \r
    \r*****************************""")


def create_file(file_name):
    f = open(file_name, "x")
    f.close()


def existing_txt(directory):
    txt_files = glob(os.path.join(directory, '*.txt'))
    clean_list = []
    for element in txt_files:
        clean_list.append(element[2:])
    # https://flexiple.com/python/convert-list-to-string-python
    print(" ".join(clean_list))


def write_line(file_name, line):
    with open(file_name, 'a') as f:
        f.write(f"{line}\n")


def display_file(file_name):
    """Affiche le contenu d'un fichier"""
    file = open(file_name, 'r')
    file_lines = file.readlines()
    file.close()
    print("\n*********************\n")
    print(f"Voici le contenu du fichier {file_name}:")
    # https://www.simplilearn.com/tutorials/python-tutorial/strip-in-python
    [print(line.strip()) for line in file_lines]


def tables_mult():
    # https://www.pythonforbeginners.com/basics/how-to-clear-a-text-file-in-python - open in 'w' mode to have it cleared each time
    with open('tables.txt', 'w') as f:
        for num_table in range(2, 31):
            f.write(f"\nVoici la table de {num_table}\n")
            for loop in range(1, 21):
                line = f"{num_table} * {loop} = { num_table * loop}"
                f.write(f"{line}\n")


def triple_space(file_name):
    file = open(file_name, 'r')
    file_lines = file.readlines()
    for line in file_lines:
        words = line.split(" ")
        new_line = "   ".join(words)
        write_line(f"triple_{file_name}", new_line)
    file.close()
    display_file(f"triple_{file_name}")


def fusion_files(file_name_A, file_name_B):
    file_A = open(file_name_A, 'r')
    file_lines_A = file_A.readlines()
    file_A.close()

    file_B = open(file_name_B, 'r')
    file_lines_B = file_B.readlines()
    file_B.close()

    step_1 = min(len(file_lines_A), len(file_lines_B))
    step_2 = max(len(file_lines_A), len(file_lines_B))

    file_C = open('fusion.txt', 'w')
    for i in range(step_1):
        file_C.write(file_lines_A[i])
        file_C.write(file_lines_B[i])
    for i in range(step_1, step_2):
        if len(file_lines_A) > len(file_lines_B):
            file_C.write(file_lines_A[i])
        else:
            file_C.write(file_lines_B[i])
    file_C.close()
    display_file('fusion.txt')


def app():

    while True:
        choice = input("""
            \nQue voulez vous faire?
            \rA - Enregistrer de nouvelles lignes de texte ?
            \rB - Afficher le contenu d'un fichier ?
            \rC - réviser les tables de multiplication?
            \rD - recopier in texte en triplant les espaces ?
            \rE - fusionner 2 fichiers texte ?
            \rQ - Pour quitter
            \rC'est à vous: """)

        # Ecrire dans un fichier en le créant si besoin
        if choice.upper() == 'A':
            file_name = input("\nEntrez le nom du fichier texte: ")
            line = input("Entrez une nouvelle ligne puis pressez enter: ")
            while line != '':
                write_line(file_name, line)
                line = input("Entrez une nouvelle ligne puis pressez enter: ")
            display_file(file_name)

        # Display the content of a file
        elif choice.upper() == 'B':
            file_name = input("\nEntrez le nom du fichier texte: ")
            # vérifier si le fichier existe déjà
            """https://www.simplilearn.com/tutorials/python-tutorial/python-check-if-file-exists"""
            if isfile(f"./{file_name}"):
                display_file(file_name)
            else:
                print(
                    "Ce fichier n'existe pas. Vous pouvez consulter les fichiers txt suivants:\n ")
                existing_txt('.')

        # réviser les tables de multiplication
        elif choice.upper() == "C":
            tables_mult()
            display_file('tables.txt')

        # tripler les espaces entre les mots d'un texte
        elif choice == "D":
            file_name = input("\nEntrez le nom du fichier texte: ")
            triple_space(file_name)

        # fusionner 2 fichiers texte
        elif choice.upper() == "E":
            file_name_A = input("Nom du premier fichier à fusionner: ")
            file_name_B = input("Nom du deuxième fichier à fusionner: ")
            fusion_files(file_name_A, file_name_B)

        # To quit the app
        elif choice.upper() == 'Q':
            print("\n*********************\n")
            print("A bientôt\n")
            return


if __name__ == "__main__":
    app()


# ************************************************************************
# *********************** EXO 9 ******************************************
# ************************************************************************


print(
    f"""*****************************
    \nEXERCICE 9 - quelques notes
    \r
    \r*****************************""")


def save_list(list_name, name):
    pickle_out = open(f"{name}.pickle", "wb")
    pickle.dump(list_name, pickle_out)
    pickle_out.close()


def open_list(name):
    # https://pythonprogramming.net/python-pickle-module-save-objects-serialization/
    pickle_in = open(f"{name}.pickle", "rb")
    return pickle.load(pickle_in)


def display_lists():
    pass


def existing_pickle(directory):
    pickle_files = glob(os.path.join(directory, '*.pickle'))
    clean_list = []
    for element in pickle_files:
        clean_list.append(element[2:-7])
    # https://flexiple.com/python/convert-list-to-string-python
    print(" ".join(clean_list))


def enter_notes(list_notes=[]):

    while True:
        note = input("\nNouvelle note: ")
        if note == '':
            print("See you soon")
            break
        else:
            try:
                note = int(note)
                if note > 20 or note < 0:
                    raise ValueError(
                        "Attention la note doit être entre 0 et 20")
            except ValueError as err:
                if "base 10" in str(err):
                    print("saisie incorrecte.")
                else:
                    print(err)
            else:
                list_notes.append(note)
                number_of_notes = len(list_notes)
                average = sum(list_notes) / number_of_notes
                print(f"""
                    \nNombre de notes: {number_of_notes}
                    \rMoyenne des notes: {round(average, 1)}
                    \rNote la plus basse: {min(list_notes)}
                    \rNote la plus haute: {max(list_notes)}
                    """)
    return list_notes


def app():
    choice = input("""
                \nBienvenue dans le module de saisie des notes.
                \rQue voulez vous faire ?
                \rA - Continuer une liste existante?
                \rB - Voulez vous créer une nouvelle liste?
                \rC - Voulez vous écraser une liste existante?
                \rQ - Voulez vous sortir ?
                \rC'est à vous: """)

    if choice.upper() == "A":
        # continuer liste existante
        print("The available lists are: ")
        existing_pickle('./')
        name = input("What is the name of the list?")
        list_notes = open_list(name)
        # print(list_notes)
        print(f"List {name}:")
        list_notes = enter_notes(list_notes)
        # print(list_notes)
        save_list(list_notes, name)
        pass

    elif choice.upper() == "B":
        # nouvelle list
        name = input("What is the name of the new list?")
        list_notes = enter_notes()
        # print(list_notes)
        save_list(list_notes, name)

    elif choice.upper() == "C":
        print("The available lists are: ")
        existing_pickle('./')
        name = input("What is the name of the list?")
        list_notes = enter_notes()
        # print(list_notes)
        save_list(list_notes, name)

    elif choice.upper() == 'Q':
        print("See you soon")
        return


if __name__ == "__main__":
    app()


# ************************************************************************
# *********************** EXO 10 *****************************************
# ************************************************************************


# https://realpython.com/python-json/
# https://pynative.com/python-save-dictionary-to-file/


print(
    f"""*****************************
    \nEXERCICE 10 - première base de données
    \r
    \r*****************************""")

persons = {
    "dora":  (18, "F", 1.50),
    "miloy": (16, "F", 1.60),
    "tonio": (15, "M", 1.80),

}

# remplissage du dictionnaire : ajout d'informations


def add_person(dict):
    adding_other = True
    while adding_other:
        name = input("Nom: ")
        age = input("Age: ")
        sexe = input("Sexe: ")
        taille = input("Taille: ")
        dict[name] = (age, sexe, taille)
        response = input("Press A to add other person and enter to finish")
        if response != 'A':
            adding_other = False
    return dict


# consultation du dictionnaire
def consult_persons(dict, name):

    if name in dict.keys():
        print(
            f"Nom : {name} - âge : {dict[name][0]} ans - sexe : {dict[name][1]} - taille : {dict[name][2]} m")
    else:
        print("Cette personne n'est pas dans le dictionnaire. ")


def dict_to_json(dict):
    # serialization
    with open("persons.json", "w") as write_file:
        json.dump(dict, write_file, indent=4)  # encode dict into JSON


def json_to_dict():
    # deserialization
    with open("persons.json", "r") as read_file:
        list_persons = json.load(read_file)
    return list_persons


def startupCheck():
    # https://stackoverflow.com/questions/32991069/python-checking-for-json-files-and-creating-one-if-needed

    if os.path.isfile("persons.json") and os.access("persons.json", os.R_OK):
        # checks if file exists
        # print("File exists and is readable")
        return

    else:
        print("Either file is missing or is not readable, creating file...")
        with io.open("persons.json", 'w') as db_file:
            db_file.write(json.dumps({}))


def app():
    while True:
        startupCheck()
        person_dict = json_to_dict()

        choice = input("""
            \nWhat do you want to do ?
            \rA - Add a person ?
            \rB - Consult the list of persons?
            \rQ - Quit
            \rC'est à vous: """)

        if choice.upper() == "A":
            person_dict = add_person(person_dict)
        elif choice.upper() == "B":
            print("Available entries")
            [print(key) for key in person_dict.keys()]
            name = input("Which person are you interested in? ")
            consult_persons(person_dict, name)
        elif choice.upper() == 'Q':
            print("Goodbye")
            return
        dict_to_json(person_dict)


if __name__ == "__main__":
    app()
