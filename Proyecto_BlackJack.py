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
    
    if modoEjecucion == 'J':
        print ("MODO JUEGO SELECCIONADO")
        
    else if modoEjecucion == 'A':
        print ("MODO ANALISIS SELECCIONADO")
    
    else if modoEjecucion == '':
        print ("MODO JUEGO PREDETERMINADO")
        
    else modoEjecucion != 'J' or modoEjecucion != 'A':
        print ("Entrada no valida, inserte de nuevo el modo de ejecución")
        print ("Modos de ejecucion: [J]uego [A]nalisis")
        modoEjecucion = input ("Modo de ejecucion: ")
    
