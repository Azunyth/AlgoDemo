from random import randint

def defineTurn(turn):
    player = "Joueur"
    if turn%2:
        player = "Ordinateur"

    return player

def playTurn(turn, nbMatchesLeft):
    nbMatchesPicked = 0
    player = defineTurn(turn)

    print("Tour {} ! Il reste {} allumettes".format(turn, nbMatchesLeft))

    if not turn%2:
        nbMatchesPicked = playerMove(nbMatchesLeft)
    else:
        nbMatchesPicked = iaMove(nbMatchesLeft)

    print("{} a retiré {} allumette(s)".format(player, nbMatchesPicked))
    print("-------------------------------------------")

    return nbMatchesLeft - nbMatchesPicked

def iaMove(nbMatchesLeft):
    nbMatchesPicked = 0
    """
    Toute petite IA, si il reste entre 2 et 4 allumettes,
    l'ordinateur retire de quoi laisser une allumette
    Sinon, il retire aléatoirement entre 1 et 3 allumettes
    """
    if nbMatchesLeft > 1 and nbMatchesLeft <= 4:
        nbMatchesPicked = nbMatchesLeft - 1
    else:
        nbMatchesPicked = randint(1,3)

    return nbMatchesPicked

def playerMove(nbMatchesLeft):
    nbMatchesPicked = 0

    while nbMatchesPicked < 1 or nbMatchesPicked > 3:
        nbMatchesPicked = eval(input("Nombre d'allumettes à retirer : "))

    return nbMatchesPicked

def initGame():
    nbMatches = 0
    while nbMatches < 1:
        nbMatches = eval(input("Avec combien d'allumettes voulez vous jouer ? "))

    return nbMatches

def checkWinner(turn, nbMatchesLeft):
    player = defineTurn(turn)
    # Le premier if verifie le gagnant, l'ordinateur ne depassera jamais le seuil quoiqu'il arrive
    # Par contre nous verifions que le joueur n'est pas en train de se faire perdre et si c'est le cas
    # nous declarons le joueur du tour suivant (l'ordinateur donc) gagnant !
    if nbMatchesLeft == 1:
        print(player, " a gagné !")
    elif nbMatchesLeft < 1:
        print(defineTurn(turn+1), " a gagné !")

def launchGame():
    nbMatches = initGame()
    turn = 0

    while nbMatches > 1:
        nbMatches = playTurn(turn, nbMatches)
        checkWinner(turn, nbMatches)
        turn += 1


"""
PROGRAMME PRINCIPAL
"""
launchGame()
