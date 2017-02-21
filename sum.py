nb = eval(input("Saisir un nombre : "))

totalSum = 0
totalFacto = 1

for i in range(1,nb+1):
    totalSum += i
    totalFacto *= i

print("Somme des nombres jusqu'à ",nb," : ",totalSum);
print("Factoriel de ",nb," : ",totalFacto);
