
async def printGriglia(matrix):

    for i in range(len(matrix)):

        string = ''

        for j in range(len(matrix[i])-1):
            string += matrix[i][j] + "|"

        string += matrix[i][-1]
        print(string)

        # print("-" * ((len(matrix)*2)-1))

    return

# Questa Funzione funziona solo per matrici quadrate
async def Scan_Diagonals(matrix, elem):

    D1_Different = False
    D2_Different = False

    # Controlliamo la Diagonale Negativa
    i = 0
    # Diamo per scontato la matrice sia quadrata
    while ((i < len(matrix)) and (not D1_Different)):

        if (matrix[i][i] != elem):
            D1_Different = True

        i += 1

    # Controlliamo la Diagonale Positiva
    i = 0
    while ((i < len(matrix)) and (not D2_Different)):

        if (matrix[(len(matrix) - 1) - i][i] != elem):
            D2_Different = True

        i += 1

    # Solo se tutti e due i valori sono VERI allora il vincitore NON ha vinto
    # Se vi è anche solo un falso allora ha vinto

    return not (D1_Different and D2_Different)

async def Scan_Row(matrix, y, elem):

    '''
    :param matrix:
    :param y:     Coordinata della riga
    :param elem:
    :return:
    '''

    Row_Different = False

    for j in range(len(matrix[y])):

        if (matrix[y][j] != elem):
            Row_Different = True

    # Se la riga è tutta uguale il giocatore ha vinto

    return (not Row_Different)

async def Scan_Column(matrix, x, elem):

    '''
    :param matrix:
    :param x:     Coordinata della colonna
    :param elem:
    :return:
    '''

    Col_Different = False

    for i in range(len(matrix)):

        if (matrix[i][x] != elem):
            Col_Different = True

    # Se la colonna è tutta uguale il giocatore ha vinto

    return (not Col_Different)

async def Turno(matrix, elem):

    # Mi serve fare questo controlloo in modo tale da impedire che il giocatore scelga delle
    # coordinate dove si è già giocato
    Posizionato = False

    while not (Posizionato):

        cords = input("Inserire le coordinate dove giocare la prossima mossa: ")

        cord_y = int(cords[0])
        cord_x = int(cords[2])

        if (matrix[cord_y][cord_x] != "-"):
            print("Nelle coordinate inserite è già stato giocato")
        else:
            matrix[cord_y][cord_x] = elem
            Posizionato = True

    print()

    await printGriglia(matrix)

    print()

    # Controlliamo se il giocatore ha vinto o meno
    Vinto = ((await Scan_Row(matrix, cord_y, elem)) or (await Scan_Column(matrix, cord_x, elem)) or (await Scan_Diagonals(matrix, elem)))

    return Vinto

async def Partita(matrix):

    Finito = False

    i = 0
    while (Finito == False):

        if (i % 2 == 0):
            elem = "x"
        else:
            elem = "o"

        if (await Turno(matrix, elem) == True):
            print("\nIl giocatore ha vinto")
            Finito = True

        i += 1

    return

async def main():

    matrix = [

        list("---"),
        list("---"),
        list("---")
    ]

    '''print(Scan_Diagonals(matrix,"x"))

    print(Scan_Column(matrix, 0, "0"))

    print(Scan_Row(matrix, 2, "x"))'''

    await Partita(matrix)

    return

#main()
