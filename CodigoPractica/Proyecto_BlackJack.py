# file:///C:/Users/Alex/Desktop/2%C2%BA%20CUATRI/PAR/PRACTICAS/PRACTICA%201/prac2324a.pdf #
"""
Practica 1 - Paradigmas de Programación
García Lavandera, Alejandro
García del Caz, Carla
Curso 2023-2024
"""

import externo2
import os

# Genero una baraja de cartas mezclada con 2 mazos
def generamosMazo():
    estrategia = externo2.Estrategia(2)
    mazo = externo2.Mazo(MiCarta,estrategia)

    listaCartas = []
    # Calculo e inserto el indice de las cartas en listaCartas
    for i in range(103):
        valor = int(mazo.reparte().ind)
        listaCartas.append(valor)

    return listaCartas

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
            
            
            
class Mano:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cartas = []  # Inicializamos el atributo cartas como una lista vacía
        self.valor = 0
        self.estado = "A"

    def agregar_carta(self, carta):
        self.cartas.append(carta)
        self.calcular_valor()
        self.calcula_carta()

    def calcular_valor(self):
        # Inicializamos el valor en 0 antes de calcularlo nuevamente
        self.valor = 0
        num_as = 0  # Contador de ases (que valen 1 u 11)
        
        for carta in self.cartas:
            if carta % 13 + 1 in [11, 12, 13] :
                self.valor += 10
            elif carta % 13 + 1 == 1:
                num_as += 1
                self.valor += 11  # Asumimos el valor del as como 11 por defecto
            else:
                self.valor += int(carta % 13 + 1)  # Las cartas numéricas tienen su valor numérico
        
        # Ajustamos el valor de los ases si el total es mayor a 21
        while num_as > 0 and self.valor > 21:
            self.valor -= 10  # Restamos 10 al valor total por cada as
            num_as -= 1
            
    def calcula_carta(self):
        # Inicializamos el valor en 0 antes de calcularlo nuevamente
        manoMostrar = []
        
        for ind in self.cartas:
            if ind % 13 + 1 == 1:
                manoMostrar.append("A")
            elif ind % 13 + 1 == 11:
                manoMostrar.append("J")
            elif ind % 13 + 1 == 12:
                manoMostrar.append("Q")
            elif ind % 13 + 1 == 13:
                manoMostrar.append("K")
            else:
                num = ind % 13 + 1
                manoMostrar.append(num)
                
        return manoMostrar

    def abrir_mano(self):
        self.estado = "A"

    def cerrar_mano(self):
        self.estado = "C"
        
    def mano_pasada(self):
        self.estado = "P"



class Croupier():
    def __init__(self):
        self.mano = Mano("Croupier")



class Jugador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.manos = []
        self.contadorManos = 0
        self.balance = 0
        self.valor_mano = 0
        
    def agregar_mano(self):
        nombreMano = f"mano{chr(ord('A') + self.contadorManos)}"
        nuevaMano = Mano(nombreMano)
        self.manos.append(nuevaMano)
        self.contadorManos += 1
        
    def obtener_mano(self, indice):
        return self.manos[indice]

    def calcular_valor_manos(self):
        self.valor_mano = 0
        num_as = 0
        
        for num_mano in self.manos:
            
            
    def separarMano(self, indice_mano, indice_carta):
        mano_original = self.manos[indice_mano]
        carta = mano_original.cartas.pop(indice_carta)  # Quitamos la carta de la mano original
        nombre_nueva_mano = f"{mano_original.nombre}{chr(ord('A') + len(self.manos) - 1)}"
        nueva_mano = Mano(nombre_nueva_mano)  # Creamos una nueva mano para la carta separada
        nueva_mano.agregar_carta(carta)  # Agregamos la carta separada a la nueva mano
        self.manos.append(nueva_mano)  # Agregamos la nueva mano a las manos del jugador



def imprimeInfo(jugador, croupier):
    croupier.mano.calcular_valor()
    jugador.manos.calcular_valor_manos()
    print(F"<{croupier.mano.estado}>{croupier.mano.nombre} ({croupier.mano.valor}): ", croupier.mano.calcula_carta())
    print(F"<{jugador.mano.estado}>{jugador.mano.nombre} ({jugador.mano.valor}): ", jugador.mano.calcula_carta())
    print(croupier.mano.cartas)
    print(jugador.mano.cartas)


def turnoJugador(jugador, mazo):
    print("TURNO DEL JUGADOR")
    for i, mano in enumerate(jugador.manos):
        jugada = input(f"¿Jugada para {mano.nombre}? [P]edir [D]oblar [C]errar")
        
        # Pedimos carta
        if jugada in ["P", "p"]:
            cartaNueva = mazo.pop()
            mano.agregar_carta(cartaNueva)
        
        # Doblar apuesta
        elif jugada in ["D", "d"]:
            pass
        
        # Cerrar mano
        elif jugada in ["C", "c"]:
            mano.cerrar_mano()
        
        elif jugada in ["S", "s"] and len(mano.cartas) == 2 and mano.cartas[0] == mano.cartas[1] == 10:
            jugador.separar_mano(i, 0)
        
        else:
            print("Opcion no valida, por favor, inserte de nuevo.")

def modoJuego(mazo):
    # Variable que controla el bucle para jugar partidas
    finPartidas = True
    
    # Contador del balance del jugador
    balance = 0
    
    while finPartidas:
        # Contador de partidas
        countPartidas = 1
        
        print("--- INICIO PARTIDA #", countPartidas, " --- BALANCE = ", balance, "€" )
        
        apuesta = int(input("¿Apuesta? [2] [10] [50] "))
        
        # REPARTO INICIAL #
        # Creo al croupier y al jugador
        croupier = Croupier()
        jugador = Jugador("Jugador")
        # Agregamos una mano al jugador
        jugador.agregar_mano()

        separaciones(2)

        print("REPARTO INICIAL")
        # Inserto la primera carta al croupier y al jugador
        for i in range(1):
            croupier.mano.agregar_carta(mazo.pop())
            jugador.obtener_mano(0).agregar_carta(mazo.pop())
        imprimeInfo(jugador, croupier)
        
        turnoJugador(jugador, mazo)
        
        
def modoAnalisis(mazo):
    pass

def modoPredeterminado(mazo):
    pass





def clearTerminal():
    os.system('clear')
    
def separaciones(num):
    for i in range(num):
        print()
        

def Main():
    clearTerminal()
    
    print("*** BLACKJACK - PARADIGMAS DE PROGRAMACIÓN 2023/24 ***")
    
    mazo = generamosMazo()

    print("Indique el modo de ejecucion:")
    modoEjecucion = input("[J]uego [A]nalisis: ")
    
    bucleCorrecto = True
    while bucleCorrecto:
        if modoEjecucion == "J" or modoEjecucion == "j":
            modoJuego(mazo)
            
        elif modoEjecucion == "A" or modoEjecucion == "a":
            modoAnalisis(mazo)
            
        elif modoEjecucion == "":
            modoPredeterminado(mazo)
        
        else:
            separaciones(2)
            print("Opcion insertada no valida, vuelva a insertar el modo de ejecucion")
            modoEjecucion = input("[J]uego [A]nalisis:" )




if __name__ == "__main__":
    Main()