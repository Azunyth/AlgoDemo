age = eval(input("Votre age : "))
licence = eval(input("Votre nombre d'année de permis : "))
accident = eval(input("Nombre d'accident : "))
insurance = eval(input("Nombre d'année d'assurance : "))

p = 0

if(age <= 25):
    p += 1

if(licence <= 2):
    p += 1

p += accident

if(p < 3 and insurance > 1):
    p -= 1

if(p == -1):
	couleur = "bleu"
elif(p == 0):
	couleur = "vert"
elif(p == 1):
	couleur = "orange"
elif(p == 2):
	couleur = "rouge"
else:
	couleur = "refusé"

print("Situation : ", couleur)
