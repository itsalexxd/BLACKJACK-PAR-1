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
    
    def dibujacarta(self, carta):
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
    
def separaciones(espacios):
    for i in range (espacios):
        print()

class colores():
    RED = "\033[31m"
    
    
    
    
class Mano():
    def __init__(self, mano, estado):
        self.mano = mano
        self.estado = estado
    
class Croupier():
    def __init__(self, manoCrupier):
        self.muestraInfCroupier = manoCrupier
    
    def muestraInfCroupier():
        pass
    
    
class Jugador():
    def __init__(self):
        pass
    
#################
#### M A I N ####
#################

def Main():

    estrategia = externo2.Estrategia(2)
    mazo = externo2.Mazo(MiCarta,estrategia)

    listaCartas = []
    # Calculo e inserto el indice de las cartas en listaCartas
    for i in range(51):
        valor = int(mazo.reparte().ind)
        listaCartas.append(valor)
    
    for i in range(5):
        carta = MiCarta(listaCartas[i])
        carta.dibujacarta(carta)
        
    print(listaCartas)
    
    # Genero un array con todas las cartas del mazo desordenadas
    mazoMezclado = [51]
    for i in range(mazoMezclado):
        posCarta = int(mazo.reparte().ind)
        mazoMezclado.append(posCarta)



    # LIMPIO EL TERMINAL #
    clearTerminal()


    # INICIAMOS EL JUEGO PIDIENDO MODO DE EJECUCION #
    print("Indique el modo de ejecucion:")
    modoEjecucion = input("[J]uego [A]nalisi:")
    
    bucle1 = False
    
    while bucle1 == False:
        if modoEjecucion == "J" or modoEjecucion == "j":
            bucle1 = True
            separaciones(2)
            print("### MODO JUEGO SELECCIONADO ###")
            print()
            
            balance = 0
            print("--- INICIO DE LA PARTIDA #1 --- BALANCE = ", balance, " €")
            print()
            apuesta = int(input("¿Apuesta? [2] [10] [50]"))
            
            while bucle1 == True:
                apuestasValidas = {2, 10, 50}
                if apuesta in apuestasValidas:
                    bucle1 = False
                    print()
                    print("REPARTO INICIAL:")

                    
                else:
                    print("Apuesta no valida, inserte de nuevo la apuesta deseada")
                    apuesta = input("¿Apuesta? [2] [10] [50]  ")
                    
                    





        elif modoEjecucion == "A" or modoEjecucion == "a":
            bucle1 = True
            separaciones(2)
            print("### MODO ANALISIS SELECCIONADO ###")
    
        elif modoEjecucion == "":
            bucle1 = True
            separaciones(2)
            print("### MODO JUEGO PREDETERMINADO ###")
        else:
            separaciones(2)
            print("Opcion insertada no valida, vuelva a insertar el modo de ejecucion")
            modoEjecucion = input(colores.RED + "[J]uego [A]nalisi:" + colores.RED)


if __name__ == "__main__":
    Main()