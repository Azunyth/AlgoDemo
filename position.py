nb = eval(input("Saisir un nombre : "))

maxNumber = 0
maxPosition = currentPosition = 1

while nb != 0:                  # tant que l'utilisateur saisi un nombre différent de 0
    if nb > maxNumber:          # si le nombre saisi est plus grand que le nombre tampon
        maxNumber = nb          # on affecte alors ce nombre
        maxPosition = currentPosition # on affecte également la position courrante

    currentPosition += 1        # on met a jour la position courrante
    nb = eval(input("Saisir un nombre : ")) # on propose a l'utilisateur de choisir un nouveau nombre

print("Le plus grand nombre est le {} qui a été saisi en {}e position".format(maxNumber, maxPosition));
