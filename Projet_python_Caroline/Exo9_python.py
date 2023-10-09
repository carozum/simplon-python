import pickle
import os
from glob import glob


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
    pickle_in = open(f"{name}.pickle", "rb")
    return pickle.load(pickle_in)


def display_lists():
    pass


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


def existing_pickle(directory):
    pickle_files = glob(os.path.join(directory, '*.pickle'))
    clean_list = []
    for element in pickle_files:
        clean_list.append(element[2:])
    # https://flexiple.com/python/convert-list-to-string-python
    print(" ".join(clean_list))


def app():
    choice = input("""
                \nBienvenue dans le module de saisie des notes.
                \rQue voulez vous faire ?
                \rA - Continuer une liste existante?
                \rB - Voulez vous créer une nouvelle liste?
                \rC - Voulez vous écraser une liste existante?
                \rQ - Voulez vous sortir ?""")

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
        print(list_notes)
        save_list(list_notes, name)

    elif choice.upper() == "C":
        pass
    elif choice.upper() == 'Q':
        print("See you soon")
        return ''


# https://pythonprogramming.net/python-pickle-module-save-objects-serialization/


if __name__ == "__main__":
    app()
