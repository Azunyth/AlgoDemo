i = 0
tab = []

while i < 5:
    nb = eval(input("Saisir une valeur positive : "))
    while nb < 0:
        nb = eval(input("Une vraie valeur positive ... : "))
    tab.append(nb)
    i+=1

for i in range(10):
    for j in range(len(tab)):
        print(tab[j])

# Alternative

for i in range(10):
    for val in tab:
        print(val)
