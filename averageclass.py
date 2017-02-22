i = 0
notes = []
total = 0
average = 0
nbNoteAboveAverage = 0

nb = eval(input("Saisir une note : "))

while nb != -1:
    notes.append(nb)
    total += nb  # on additione au fur et a mesure les saisies utilisateur
    nb = eval(input("Saisir une note : "))

average = total / len(notes)

for note in notes:
    if note > average:
        nbNoteAboveAverage += 1
    # Alternative
    # nbNoteAboveAverage += note > average


print("La moyenne est de ", average, " et il y a ", nbNoteAboveAverage, " notes supérieures à la moyenne");
