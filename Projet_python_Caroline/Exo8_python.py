# source : https://www.pythontutorial.net/python-basics/python-read-text-file/

import os
from os.path import isfile
from glob import glob

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
