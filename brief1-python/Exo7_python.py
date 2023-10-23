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
