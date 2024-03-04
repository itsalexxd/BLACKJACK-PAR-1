def verMatriz(matriz):
    for i in range(3):
        for j in range(3):
            print (matriz[i][j], end="")


if __name__ == "__name__":
    matriz = [[4,1,5], [3,2,4], [9,0,1]]
    verMatriz(matriz)
    