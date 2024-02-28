# file:///C:/Users/Alex/Desktop/2%C2%BA%20CUATRI/PAR/PRACTICAS/PRACTICA%201/prac2324a.pdf #
"""
Practica 1 - Paradigmas de Programación
García Lavandera, Alejandro
García del Caz, Carla
Curso 2023-2024
"""

if __name__ == "__main__":
    
    # Pido el modo de ejecucion en el que desea iniciar el programa
    print ("Modos de ejecucion: [J]uego [A]nalisis")
    modoEjecucion = input ("Modo de ejecucion: ")
    
    if modoEjecucion == 'J':
        print ("MODO JUEGO SELECCIONADO")
        
    if modoEjecucion == 'A':
        print ("MODO ANALISIS SELECCIONADO")
        
    if modoEjecucion != 'J' || modoEjecucion != 'A':
        print ("Entrada no valida, inserte de nuevo el modo de ejecución")
        print ("Modos de ejecucion: [J]uego [A]nalisis")
        modoEjecucion = input ("Modo de ejecucion: ")
    
