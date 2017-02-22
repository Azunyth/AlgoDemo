i = 0
tab = []

while i < 5:
    nb = eval(input("Saisir une valeur positive : "))
    while nb < 0:
        nb = eval(input("Une vraie valeur positive ... : "))
    tab.append(nb)
    i+=1

print(tab)
