age = eval(input("Entrer votre age : "))

if age < 0:
    print("Oops, age incorrect")
else : 
    if age > 0 and age <= 14:
        print("Enfant")
    elif age >= 15 and age <= 18:
        print("Ado")
    elif age >= 19 and age <= 30:
        print("Jeune")
    elif age >= 31 and age <= 50:
        print("Cadre")
    elif age >= 51 and age <= 65:
        print("Senior")
    elif age >= 66 and age <= 110:
        print("Retraité")
    else:
        print("Menteur")
