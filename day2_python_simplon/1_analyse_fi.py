# données
rev = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44,
       11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
dep = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20,
       3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]


# fonction qui présente une liste en K€ avec 2 chiffres après la virgule
def format_euros(list_euros):
    return [round(element/1000) for element in list_euros]


# calcul du bénéfice : revenus moins dépenses
benef = [round(a-b, 2) for a, b in zip(rev, dep)]
benef_k = format_euros(benef)

# calcul du bénéfice net: bénéfice net impôt de 30%
benef_net = [round(element * (1 - 30/100), 2) for element in benef]
benef_net_k = format_euros(benef_net)

# marge bénéficiaire
marge = [f"{round(bn / r * 100)}%" for bn, r in zip(benef_net, rev)]
marge_annuelle = round(sum(benef_net)/sum(rev) * 100)

# bons mois
benef_moyen = round(sum(benef) / len(benef), 2)
bons_mois = []
bons_benefs = []
mauvais_mois = []
mauvais_benefs = []
for i in range(len(benef)):
    if benef[i] > benef_moyen:
        bons_mois.append(i+1)
        bons_benefs.append(benef[i])
    else:
        mauvais_mois.append(i+1)
        mauvais_benefs.append(benef[i])

pire = min(mauvais_benefs)
index_pire = mauvais_benefs.index(pire)
pire_mois = mauvais_mois[index_pire]
print(pire_mois)
