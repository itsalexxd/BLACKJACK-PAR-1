import math

def expresiones():
    print ("###############################")
    print ("#### E J E R C I C I O - 1 ####")
    print ("###############################")

    print ()
    
    print("Escriba las siguientes expresiones en Python. Guarde el resultado en una variable y muestrelo por pantalla:")
    
    valorA = 3*5/2+3    
    print ("a) ", valorA)
    
    valorB = math.sqrt(7+9) * 2
    print ("b) ",valorB)
    
    valorC = pow((4-7), 2)
    print ("c) ", valorC)
    
    valorD = 6 % 4
    print ("d) ", valorD)


def conseguirListas():
    print ("###############################")
    print ("#### E J E R C I C I O - 2 ####")
    print ("###############################")
    
    print ()
    
    print ("Dada la lista a = [1,2,3,4,5,6], indique la expresion para obtener las siguientes listas partiendo de la lista a y utilizando el operador [i:j]")    
    a = [1,2,3,4,5,6]
    
    apartadoA = [0,2]
    print ("a) ", apartadoA)
    
    apartadoB = [1,2,3]
    print ("b) ", apartadoB)
    
    apartadoC = [3,4,5]
    print ("c) ", apartadoC)
    
def indicaListas():
    print ("###############################")
    print ("#### E J E R C I C I O - 3 ####")
    print ("###############################")
    
    print ()
    
    print ("Indique cuales son las listas generadas usando la funcion range()")

    a = range(10)
    print ("a) ", a )

    b = range(1,10)
    print ("b) ", b )
    
    c = range(1,10,2)
    print ("c) ", c )

    

def verMatriz():
    print ("###############################")
    print ("#### E J E R C I C I O - 6 ####")
    print ("###############################")
    
    print ()
    
    print ("Representa la siguiente matriz en Python:")
    
    matriz = [[4,1,5],[3,2,4],[9,0,1]]
    for i in range(3):
        for j in range(3):
            print (matriz[i][j], end=" ")
        print()


if __name__ == "__main__":
    
    print()
    print()
    
    # Ejercicio 1
    expresiones()
    
    print()
    print()
    
    # Ejercicio 2
    conseguirListas()
    
    print()
    print()
    
    # Ejercicio 3
    indicaListas()
    
    print()
    print()
    
    # Ejercicio 6
    verMatriz()
    