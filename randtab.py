from random import randint

tab = []
nbPositiv = 0
nbNegativ = 0

for i in range(10):
    rand = randint(-100,100)
    tab.append(rand)
    # on regarde si le nombre généré est positif ou négatif
    # on incrémente le bon compteur
    if(rand>=0):
        nbPositiv += 1
    else:
        nbNegativ +=1
    # Alternative
    # nbPositiv += rand >= 0

print("Nombre de positif : ", nbPositiv)
print("Nombre de négatif : ", nbNegativ)

# Alternative
# print("Nombre de positif : ", nbPositiv)
# print("Nombre de négatif : ", len(tab)-nbPositiv)
