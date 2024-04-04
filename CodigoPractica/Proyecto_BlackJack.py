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
        self.estado = "Cerrada"

    def agregar_carta(self, carta):
        self.cartas.append(carta)
        self.calcular_valor()

    def calcular_valor(self):
        # Inicializamos el valor en 0 antes de calcularlo nuevamente
        self.valor = 0
        num_as = 0  # Contador de ases (que valen 1 u 11)
        
        for carta in self.cartas:
            if carta in ["J", "Q", "K"]:
                self.valor += 10
            elif carta == "A":
                num_as += 1
                self.valor += 11  # Asumimos el valor del as como 11 por defecto
            else:
                self.valor += int(carta)  # Las cartas numéricas tienen su valor numérico
        
        # Ajustamos el valor de los ases si el total es mayor a 21
        while num_as > 0 and self.valor > 21:
            self.valor -= 10  # Restamos 10 al valor total por cada as
            num_as -= 1

    def abrir_mano(self):
        self.estado = "Abierta"

    def cerrar_mano(self):
        self.estado = "Cerrada"
        
class Croupier():
    def __init__(self):
        self.mano = Mano("Croupier")
    
class Jugador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.balance = 0



def modoJuego(mazo):
    # Variable que controla el bucle para jugar partidas
    finPartidas = True
    
    # Contador del balance del jugador
    balance = 0
    
    while finPartidas:
        # Contador de partidas
        countPartidas = 1
        
        print("--- INICIO PARTIDA #", countPartidas, " --- BALANCE = ", balance, "€" )
        
        apuesta = int(input("¿Apuesta? [2] [10] [50]"))
        
        # REPARTO INICIAL #
        # Creo al croupier y al jugador
        croupier = Croupier()
        jugador = Jugador("Jugador")
        
        
        # Inserto la primera carta al croupier y al jugador
        for _ in range(2):
            croupier.mano.agregar_carta(mazo.pop())
            jugador.mano.agregar_carta(mazo.pop())
        
            print(f"Estado de la mano del croupier: {croupier.mano.estado}")
        print(f"Valor de la mano del croupier: {croupier.mano.valor}")
        print(f"Estado de la mano de {jugador.nombre}: {jugador.mano.estado}")
        print(f"Valor de la mano de {jugador.nombre}: {jugador.mano.valor}")
        
        print("REPARTO INICIAL")
        
        
        
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
    modoEjecucion = input("[J]uego [A]nalisi:")
    
    if modoEjecucion == "J" or modoEjecucion == "j":
        modoJuego(mazo)
        
    elif modoEjecucion == "A" or modoEjecucion == "a":
        modoAnalisis(mazo)
        
    else:
        modoPredeterminado(mazo)




if __name__ == "__main__":
    Main()