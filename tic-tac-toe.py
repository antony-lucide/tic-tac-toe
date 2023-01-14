def affichage(plateau): #Affichage du plateau
    for x in range(len(plateau)):
        for o in range(len(plateau)):
            if( plateau [x][o] == 1):
                print("x", end="")
            elif(( plateau [x][o] == 2)):
                print("o", end="")
            else:
                print(" ", end="")
        print("")

plateau = [[0,0,0],[0,0,0],[0,0,0]] #Position 0,1 0,2 0,0 etc

affichage(plateau)

def joueurs(plateau,joueurs):
    
    while(True):
        colonne = input("colonne")
        ligne = input("ligne")
        if(0 <= int (colonne) <= 2 and 0 <= int (ligne) <= 2 and plateau[int (ligne)][ int (colonne)] == 0 ):
            break
    plateau[ int (ligne)] [ int (colonne)] = joueurs #Joueurs, position et ligne

    if(rule(colonne,ligne,joueurs,plateau)):
        print("Tu as gagné")


def rule(colonne,ligne,joueurs,plateau):
    for i in range(2): #Définie les valeurs a checker
        if(plateau[i][0] == plateau[i][1] == plateau[i][2]): #si les valeurs sont égals à la position de l'autre, alors return la fonction
          return(True)
        elif(plateau[0][i] == plateau[1][i] == plateau[2][i]):
            return(True)
    if(plateau[0][0] == plateau[1][1] == plateau[2][2]): #Check la diagonale
            return(True)
    elif(plateau[2][0] == plateau[1][1] == plateau[0][2]):
        return(True)
    else: #si les deux autres conditions sont pas remplis, alors ne rien remplir
        return(None)

           





while(True): #Rendre infinie ma boucle
    joueurs(plateau,1)
    affichage(plateau)
    joueurs(plateau,2)
    affichage(plateau)

    