import io
import json
import os

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
