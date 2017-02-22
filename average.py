i = 0
tab = []
total = 0

while i < 5:
    nb = eval(input("Saisir une valeur positive : "))
    while nb < 0:
        nb = eval(input("Une vraie valeur positive ... : "))
    tab.append(nb)
    total += nb  # on additione au fur et a mesure les saisies utilisateur
    i+=1

print(total/len(tab)) # On divise le total par la taille du tableau pour la moyenne
