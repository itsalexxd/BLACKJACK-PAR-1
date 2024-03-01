# file:///C:/Users/Alex/Desktop/2%C2%BA%20CUATRI/PAR/PRACTICAS/PRACTICA%201/prac2324a.pdf #
"""
Practica 1 - Paradigmas de Programación
García Lavandera, Alejandro
García del Caz, Carla
Curso 2023-2024
"""

if __name__ == "__main__":
    
    # Pedimos el modo de ejecucion en el que desea iniciar el programa
    print ("Modos de ejecucion: [J]uego [A]nalisis")
    modoEjecucion = input ("Modo de ejecucion: ")
    
    print (" ")
    
    numPartida = 0
    balance = 0
    
    if modoEjecucion == 'J':
        
        # Sumo 1 a la cuenta de las partidas
        numPartida += numPartida + 1
        
        print ("MODO JUEGO SELECCIONADO")
        print (" ")
        print ("--- INICIO DE LA PARTIDA #" + str(numPartida) + " --- BALANCE = " + str(balance) + "€")
        print (" ")
        apuesta = input ("Seleccione la apuesta que desea realizar: [2] [10] [50]: ")
        
        
    elif modoEjecucion == 'A':
        print ("MODO ANALISIS SELECCIONADO")
    
    elif modoEjecucion == '':
        print ("MODO JUEGO PREDETERMINADO")
        
    else:
        print ("Entrada no valida, inserte de nuevo el modo de ejecución")
        print ("Modos de ejecucion: [J]uego [A]nalisis")
        modoEjecucion = input ("Modo de ejecucion: ")
    
