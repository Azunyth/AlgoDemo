hour = eval(input("Entrer une heure : "))
minutes = eval(input("Entrer des minutes : "))

if minutes == 59:
    if hour == 23:
        hour = "00"
        minutes = "00"
    else:
        hour += 1
        minutes = "00"
else:
    minutes += 1

print("{}:{}".format(hour, minutes))
