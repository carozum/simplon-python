"""Exercice 7 : manipulations de dictionnaires
Écrire une fonction qui échange les clés et les valeurs d'un dictionnaire (ce qui permettra par exemple de transformer un dictionnaire anglais/français en un dictionnaire français/anglais). On suppose qu’il n’y a pas de valeurs en double pour simplifier."""


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
