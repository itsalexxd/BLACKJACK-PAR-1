import math

def expresiones():
    print ("###############################")
    print ("#### E J E R C I C I O - 1 ####")
    print ("###############################")

    print ()
    
    print("Escriba las siguientes expresiones en Python. Guarde el resultado en una variable y muestrelo por pantalla:")
    
    print ()
    
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
    
    print ()
    
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
    
    print ()

    a = range(10)
    print ("a) ", list(a) )

    b = range(1,10)
    print ("b) ", list(b) )
    
    c = range(1,10,2)
    print ("c) ", list(c) )

    return(a,b,c)


def expresionesListas():
    print ("###############################")
    print ("#### E J E R C I C I O - 4 ####")
    print ("###############################")

    print ()
    
    print ("Partiendo de las listas a,b,c del ejercicio anterior, indica que se obtiene con las expresiones siguientes:")
    
    print ()
    
    a = range(10)
    b = range(1,10)
    c = range(1,10,2)
    
    suma = list(a) + list(b)
    producto = list(c) * 3
    
    print ("a) ", len(a))
    print ("b) ", len(b))
    print ("c) ", len(c))
    print ("d) ", suma)
    print ("e) ", producto)
    


def accederListas():
    print ("###############################")
    print ("#### E J E R C I C I O - 5 ####")
    print ("###############################")

    print ()
    
    print ("Se puede definir una matriz como mat = [[1,2,3], [4,5,6], [7,8,9]]:")
    
    print ()   
    
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    
    print ("a) Accede al elemento (1,2): ", mat[0][2])
    
    print ("b) Obten la primera fila: ", mat[0])
            
    


def verMatriz():
    print ("###############################")
    print ("#### E J E R C I C I O - 6 ####")
    print ("###############################")
    
    print ()
    
    print ("Representa la siguiente matriz en Python:")
    
    print ()
    
    matriz = [[4,1,5],[3,2,4],[9,0,1]]
    for i in range(3):
        for j in range(3):
            print (matriz[i][j], end=" ")
        print()

def insertaDiccionarioVacio():
    print ("###############################")
    print ("#### E J E R C I C I O - 7 ####")
    print ("###############################")
    
    print ()
    
    print ("Partiendo de un diccionario vacio mundial=() inserte los siguientes elementos")
    print ("Spain - 12")
    print ("Netherlands - 11")
    print ("Italy - 10")
    print ("Germany - 8")
    print ("France - 6")
    print ("Portugal - 5")
    
    print ()

    mundial = {}

    print ("Mundial (Vacio)", mundial)

    mundial["Spain"] = 12
    mundial["Netherlands"] = 11
    mundial["Italy"] = 10
    mundial["Germany"] = 8
    mundial["France"] = 6
    mundial["Portugal"] = 5
    
    print ("Mundial (Insertado)", mundial)
    
    return mundial
    
    
def gestionaLista(mundial):
    print ("###############################")
    print ("#### E J E R C I C I O - 8 ####")
    print ("###############################")
    
    print ()
    
    print ("Sobre el diccionario del apartado anterior: ")
    
    print ()
    
    print ("a) Imprime el diccionario con la sentencia 'print': ", mundial)
    print ("b) Obtenga el valor de la clave 'Spain': ", mundial["Spain"])
    print ("c) Obtenga el valor de la clave 'Portugal': ", mundial["Portugal"])
    mundial["Spain"] += 3
    print ("d) Incremente el valor de Spain en 3: ", mundial["Spain"])
    mundial["France"] -= 2 
    print ("e) Decremente el valor de Francia en 2: ", mundial["France"])
    

    
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
    
    # Ejercicio 4
    expresionesListas()
    
    print()
    print()
    
    # Ejercicio 5
    accederListas()
    
    print()
    print()
    
    # Ejercicio 6
    verMatriz()
    
    print ()
    print ()
    
    # Ejercicio 7
    mundial = insertaDiccionarioVacio()
    
    
    print ()
    print ()
    
    # Ejercicio 8
    gestionaLista(mundial)
    