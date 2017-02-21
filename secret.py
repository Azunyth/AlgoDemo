from random import randint

secret = randint(0,100)
nb = eval(input("Saisir un nombre : "))
nbTry = 2

while nb != secret and nbTry > 0:
    if nb > secret:
        print("Plus petit")
    else:
        print("Plus grand")

    nbTry -= 1
    nb = eval(input("Saisir un nombre : "))

if nb == secret:
    print("Gagné")
else:
    print("Perdu, le nombre secret était ", secret)
