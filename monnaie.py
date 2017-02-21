total = 0
bill10, bill5 = 0,0

# on demande a l'utilisateur de saisir des nombres
nb = eval(input("Saisir un nombre : "))
while nb != 0:
    total += nb
    nb = eval(input("Saisir un nombre : "))

# on lui annonce le total a payer
print("Vous devez ", total, "€")

# on lui demande le montant qu'il donne et on vérifie qu'il soit supérieur ou égal au total
amount = eval(input("Montant donnée : "))
while amount < total:
    amount = eval(input("Montant donnée : "))

# on calcul la monnaie à lui rendre
rest = amount - total

#on compte le nombre de billets de 10 à lui rendre
while rest >= 10:
    bill10 += 1
    rest -= 10

# est ce qu'il y a un billet de 5 à rendre
if rest > 5:
    rest -= 5
    bill5 += 1

print("Nombre de billets de 10 :", bill10);
print("Nombre de billets de 5 :", bill5);
print("Nombre de piecès de 1 :", rest);
