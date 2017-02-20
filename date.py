day = eval(input("Jour : "))
month = eval(input("Mois : "))
year = eval(input("Année : "))

maxDayInMonth = 31
monthValid = month >= 1 and month <= 12
dayValid = False

if monthValid:
    if(month == 2):
        maxDayInMonth = 28
        if(not year%400 or (not(year%4) and year%100)):
            maxDayInMonth += 1
    elif(month == 4 or month == 6 or month == 9 or month == 11):
        maxDayInMonth = 30

    if (day >= 1 and day <= maxDayInMonth):
        dayValid = True

if(monthValid and dayValid):
    print("Date valide")
else:
    print("Date invalide")
