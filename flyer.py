nbFlyer = eval(input("Nombre de flyers : "))

total = 0;

if nbFlyer >= 300:
    total = 100*0.15 + 200*0.1 + (nbFlyer-300)*0.06
elif nbFlyer >= 100:
    total = 100*0.15 + (nbFlyer-100)*0.1
else:
    total = nbFlyer*0.15

print("Total : ", total)
