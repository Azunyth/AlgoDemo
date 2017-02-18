sex = input("Entrer votre sexe [m/f] : ")
age = eval(input("Entrer votre age : "))

if (sex.lower() == "m" and age > 20) or (sex.lower() == "f" and age in range(18,35)):
    print("Vous payez !")
else:
    print("Vous ne payez pas.")
