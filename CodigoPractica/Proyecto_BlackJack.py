# file:///C:/Users/Alex/Desktop/2%C2%BA%20CUATRI/PAR/PRACTICAS/PRACTICA%201/prac2324a.pdf #
"""
Practica 1 - Paradigmas de Programación
García Lavandera, Alejandro
García del Caz, Carla
Curso 2023-2024
"""

import externo2
import os


# PICAS TREVOLES DIAMANTES CORAZONES ♠  ♥  ♦  ♣#
# A-10 y (J Q K) = 10
class MiCarta(externo2.CartaBase):
    # Devuelve el palo en un rango de 0-51
    @property
    def palo(self):
        if self.ind >= 0 and self.ind <= 12:
            return "♠"  # [PICAS]"
        elif self.ind >= 13 and self.ind <= 25:
            return "♣" # [TREVOLES]"
        elif self.ind >= 26 and self.ind <= 38:
            return "♦" # [DIAMANTES]"
        else:
            return "♥" # [CORAZONES]"
    
    @property
    def numCarta(self):
        
        if self.ind % 13 + 1 == 1:
            return "A"
        elif self.ind % 13 + 1 == 11:
            return "J"
        elif self.ind % 13 + 1 == 12:
            return "Q"
        elif self.ind % 13 + 1 == 13:
            return "K"
        else:
            return self.ind % 13 + 1
    
    def dibujacarta(slef, carta):
        if(super().valor) == 10:
            carta = f"""
        ╭───────╮
        │       │
        │    {super().valor} │
        │       │
        │  {carta.palo}    │
        │       │
        ╰───────╯
            """
            print(carta)
        else:
            carta = f"""
        ╭───────╮
        │       │
        │    {super().valor}  │
        │       │
        │  {carta.palo}    │
        │       │
        ╰───────╯
            """
            print(carta)

def clearTerminal():
    os.system('clear')
    
def separaciones():
    for i in range (2):
        print()



#################
#### M A I N ####
#################
def Main():
    # Limpiamos la terminal
    clearTerminal()
    
    # Pedimos al usuario que indique el modo de ejecucion del programa
    print("*** BLACKJACK - PARADIGMAS DE PROGRAMACIÓN 2023/24 ***")
    print()
    print("¿Modo de ejecucion?")
    modoEjec = input ("[J]ugar [A]nalisis: ")
    
    
    # Inicio el bucle del juego principal
    controlWhile = False
    
    while controlWhile == False:
        # Comprobamos en que modo de ejecucion desea iniciarl el usuario el programa
        
        # Modo JUEGO
        if modoEjec == 'J' or modoEjec == 'j':
            controlWhile = True
            separaciones()
            print("### MODO EJECUCION SELECCIONADO: JUEGO ###")
            
        # Modo ANALISIS
        elif modoEjec == 'A' or modoEjec == 'a':
            controlWhile = True
            separaciones()
            print("### MODO EJECUCION SELECCIONADO: ANALISIS ###")
            
        # Caso predeterminado
        elif modoEjec == '':
            controlWhile = True
            separaciones()
            print("### MODO EJECUCION SELECCIONADO: PREDETERMINADO (JUEGO) ###")
        
        # Entradas no validas
        else:
            separaciones()
            print("Entrada no valida, por favor, inserte correctamente la entrada")
            modoEjec = input ("[J]ugar [A]nalisis: ")
            
            
    


if __name__ == "__main__":
    Main()
    