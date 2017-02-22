dimension = eval(input("Dimenstion du plateau : "))
board = []

# Creation du plateau de jeu
for i in range(dimension):
    board.append([])
    for j in range(dimension):
        board[i].append(0)

# Placement du pion
x = eval(input("Position X du pion : "))
while x < 0 or x >= dimension:
    x = eval(input("Position X du pion : "))

y = eval(input("Position Y du pion : "))
while y < 0 or y >= dimension:
    y = eval(input("Position Y du pion : "))

board[x][y] = 1

for i in range(dimension):
    drawBoard = "| "
    for j in range(dimension):
        coin = "x" if board[i][j] else "."
        drawBoard += coin + " | "
    print(drawBoard)

while True:
    move = input("[Z:Haut, Q:Gauche, S:Bas, D: Droite, X:Quitter]")
    move = move.lower()
    while move not in ['z','q','s','d','x']:
        move = input("[Z:Haut, Q:Gauche, S:Bas, D: Droite, X:Quitter]")

    if move == 'x':
        break
    # On vérifie que le mouvement ne sort pas du tableau
    # si le mouvement est bon, on met a jour l'ancienne position
    if (move == 'z' and x-1 >= 0):
        board[x][y] = 0
        x-=1
    elif(move == 's' and x+1 < dimension):
        board[x][y] = 0
        x+=1
    elif(move == 'q' and y-1 >= 0):
        board[x][y] = 0
        y-=1
    elif(move == 'd' and y+1 < dimension):
        board[x][y] = 0
        y+=1

    board[x][y] = 1

    # On redessine le tableau
    for i in range(dimension):
        drawBoard = "| "
        for j in range(dimension):
            coin = "x" if board[i][j] else "."
            drawBoard += coin + " | "
        print(drawBoard)
