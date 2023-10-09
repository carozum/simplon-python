print(
    f"""*****************************
    \nEXERCICE 9 - quelques notes
    \r
    \r*****************************""")


def saisir_notes():
    list_notes = []

    while True:
        note = input("\nNouvelle note: ")
        if note == '':
            print("See you soon")
            return
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
                    \nNombre de notes saisies: {number_of_notes}
                    \rMoyenne des notes: {round(average, 1)}
                    \rNote la plus basse: {min(list_notes)}
                    \rNote la plus haute: {max(list_notes)}
                    """)


def app():
    saisir_notes()


if __name__ == "__main__":
    app()
