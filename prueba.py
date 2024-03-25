"""
Practica 1_Paradigmas de Programación
Antolín Caramazana, Ángel

"""

from externo import Mazo, Estrategia, CartaBase

class Carta (CartaBase):


    #Metodo para devolver el valor de la carta
    @property
    def valorCarta(self):

        num = super().valor

        if num == 1:
            return "A"      #Ases
        if num == 11:
            return "J"      #J
        if num == 12:
            return "Q"      #Q
        if num == 13:
            return "K"      #K
        else:
            return num
        

    #Metodo para devolver el palo
    @property
    def palos(self):

        valor = self.ind
        
        if valor >= 0 and valor <= 12:
            return "♥"
        if valor >= 13 and valor <= 25:
            return "♦"
        if valor >= 26 and valor <= 38:
            return "♣"
        else:
            return "♠"
        


    #Metodo para dibujar las cartas con el metodo deluxe
    def dibujarCarta(self):
        
        dibujo = f'''
        ╭───────╮
        │       │
        │   {self.valorCarta:<2}  │
        │       │
        │       │
        │  {self.palos}    │
        ╰───────╯
        '''
        return dibujo
        
def espacios():
    print()
    print()

def repartoIncial (mazo, jugador, crupier, cantidadJugador, cantidadCrupier):

    for _ in range (cantidadCrupier):
        crupier.append(mazo.reparte())
    for _ in range (cantidadJugador):
        jugador.append(mazo.reparte())

def mostrarManoJugador (nombre, mano):

    print("Mano de", nombre)
    
    for carta in mano:
        print(carta.dibujarCarta())




    
    





    
        
#*******************MAIN*****************************************************

def Main():

    estrategia = Estrategia(Mazo.NUM_BARAJAS)
    mazo = Mazo(Carta, estrategia)
    

    print("*** BLACKJACK - PARADIGMAS DE PROGRAMACIÓN 2023/24 ***")
    print("¿Modo de ejecución?")
    modo = input ("[J]ugar [A]nalisis: ")


    #Control bucle modo de juego
    escogerModo = True

    while escogerModo == True:

        #Modo juego
        if modo == 'J' or modo == 'j':
            
            escogerModo = False
            espacios()
            print("MODO DE JUEGO ELEGIDO: JUEGO ")

            partida = True
            balance = 0
            numPartida = 1

            while partida == True:
                
                manoCrupier = []
                manoJugador = []
                valorJugador = 0
                valorCrupier = 0


                espacios()
                print("--- INICIO DE LA PARTIDA #" ,numPartida, "--- BALANCE =" ,balance, "€")
                apuesta = input("¿Apuesta? [2] [10] [50] ")
                espacios()
                print("REPARTO INICIAL")


                repartoIncial(mazo, manoJugador, manoCrupier, 2, 1)
                

                mostrarManoCrupier(mazo, "Croupier", manoCrupier)
                mostrarManoJugador("Jugador", manoJugador)
                

                

                
                
                partida = False






        #Modo analisis
        elif modo == 'A' or modo == 'a':
            escogerModo == False
            print()
            print()
            print("MODO DE JUEGO ELEGIDO: ANALISIS")

        #Entrada predeterminada
        elif modo == '':
            escogerModo == False
            print()
            print()
            print("MODO DE JUEGO PREDETERMINADO (JUEGO)")

        #Entradas erróneas
        else:
            modo = input ("[J]ugar [A]nalisis: ")

    
    





















if __name__=="__main__":
    Main()