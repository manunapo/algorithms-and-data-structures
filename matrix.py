def printMatrix(matrix):
    for x in range(len(matrix)):
        line = "| "
        for y in range(len(matrix[x])):
            line += str(matrix[x][y]) + " "
        print(f"{line}|")


def diagonalsToList(sqMatrix):
    fdiag = []
    sdiag = []
    size = len(sqMatrix)

    for i in range(size):
        # first diagonal. up-left to down-right
        fdiag.append(sqMatrix[i][i])
        # second diagonal. up-right to down-left
        sdiag.append(sqMatrix[i][size-i-1])

    return fdiag + sdiag


def spiralToList(matrix):
    lim_rig = len(matrix[0]) - 1
    lim_bot = len(matrix) - 1
    lim_lef = 0
    lim_top = 0
    toR = []
    dir = 0
    while (lim_top <= lim_bot and lim_lef <= lim_rig):
        if dir is 0:
            for y in range(lim_lef, lim_rig + 1):
                toR.append(matrix[lim_top][y])
            dir = 1
            lim_top += 1
        elif dir is 1:
            for x in range(lim_top, lim_bot + 1):
                toR.append(matrix[x][lim_rig])
            dir = 2
            lim_rig -= 1
        elif dir is 2:
            for y in range(lim_rig, lim_lef - 1, -1):
                toR.append(matrix[lim_bot][y])
            dir = 3
            lim_bot -= 1
        elif dir is 3:
            for x in range(lim_bot, lim_top - 1, -1):
                toR.append(matrix[x][lim_lef])
            dir = 0
            lim_lef += 1
    return toR


if __name__ == '__main__':
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"--- Matrix")
    printMatrix(matrix1)
    print(f"--- ")
    print(f"Diagonals: {diagonalsToList(matrix1)}")
    print(f"Spiral: {spiralToList(matrix1)}")
    print(f"--- \n")

    matrix2 = [[1, 2, 3], [4, 5, 6]]
    print(f"--- Matrix 2")
    printMatrix(matrix2)
    print(f"--- ")
    print(f"Diagonals: {diagonalsToList(matrix2)}")
    print(f"Spiral: {spiralToList(matrix2)}")
    print(f"--- \n")

    matrix3 = [[1]]
    print(f"--- Matrix 3")
    printMatrix(matrix3)
    print(f"--- ")
    print(f"Diagonals: {diagonalsToList(matrix3)}")
    print(f"Spiral: {spiralToList(matrix3)}")
    print(f"--- \n")

    matrix4 = [[1, 2, 3, 9], [4, 5, 6, 9], [7, 8, 9, 9], [7, 8, 9, 9]]
    print(f"--- Matrix 4")
    printMatrix(matrix4)
    print(f"--- ")
    print(f"Diagonals: {diagonalsToList(matrix4)}")
    print(f"Spiral: {spiralToList(matrix4)}")
    print(f"--- \n")


    t = [1,2]
    t[0],t[1] = t[1],t[0]
    print(t)