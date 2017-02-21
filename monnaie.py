total = 0
bill10, bill5 = 0,0

nb = eval(input("Saisir un nombre : "))
while nb != 0:
    total += nb
    nb = eval(input("Saisir un nombre : "))

print("Vous devez ", total, "€")

amount = eval(input("Montant donnée : "))

rest = amount - total

while rest >= 10:
    bill10 += 1
    rest -= 10

if rest > 5:
    rest -= 5
    bill5 += 1

print("Nombre de billets de 10 :", bill10);
print("Nombre de billets de 5 :", bill5);
print("Nombre de piecès de 1 :", rest);
