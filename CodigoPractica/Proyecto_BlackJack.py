# file:///C:/Users/Alex/Desktop/2%C2%BA%20CUATRI/PAR/PRACTICAS/PRACTICA%201/prac2324a.pdf #
"""
Practica 1 - Paradigmas de Programación
García Lavandera, Alejandro
García del Caz, Carla
Curso 2023-2024
"""

import CodigoPractica.externo2 as externo2

def Main():
    # Pedimos el modo de ejecucion en el que desea iniciar el programa
    print ("Modos de ejecucion: [J]uego [A]nalisis")
    entrada = input ("Modo de ejecucion: ")
    modoEjecucion = entrada.upper()
    
    print (" ")
    
    numPartida = 0
    balance = 0
    
    ###################
    #### J U E G O ####
    ###################
    
    if modoEjecucion == 'J' or modoEjecucion == '':
        
        #temporal hasta ver como se hacen el resto de cosas para tener las variables
        manoCoupier = []
        manoJugador = []
        recuentoCoupier = 0
        recuentoJugador = 0
        manosJugador = 0
        
        if modoEjecucion == '':
            print ("MODO PREDETERMINADO PREDETERMINADO - JUEGO")
        else:
            print ("MODO JUEGO SELECCIONADO")
            
        # Sumo 1 a la cuenta de las partidas
        numPartida += numPartida + 1
        
        print (" ")
        print ("--- INICIO DE LA PARTIDA #" + str(numPartida) + " --- BALANCE = " + str(balance) + "€")
        print (" ")
        apuesta = input ("Seleccione la apuesta que desea realizar: [2] [10] [50]: ")
        print (" ")
        print ("REPARTO INICIAL:")
        print ("")
        print ("<" + str(manoCoupier) + "> Coupier (" + str(recuentoCoupier) + "): ")
        print ("")
        
        

#################################################################################################################
        
        
    #########################
    #### A N A L I S I S ####
    #########################
    
    elif modoEjecucion == 'A':
        print ("MODO ANALISIS SELECCIONADO")
        
#################################################################################################################
        
    else:
        print ("Entrada no valida, inserte de nuevo el modo de ejecución")
        print ("Modos de ejecucion: [J]uego [A]nalisis")
        modoEjecucion = input ("Modo de ejecucion: ")
    
#################################################################################################################

if __name__ == "__main__":
    Main()
    