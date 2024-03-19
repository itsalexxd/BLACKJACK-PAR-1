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

def clearTermina():
    os.system('clear')
    
def separaciones():
    for i in range (2):
        print()

#################
#### M A I N ####
#################

def Main():
    #    
    # estrategia = externo2.Estrategia(2)
    # mazo = externo2.Mazo(MiCarta,estrategia)


    # listaCartas = []
    
    # # Calculo e inserto el indice de las cartas en listaCartas
    # for i in range(51):
    #     valor = int(mazo.reparte().ind)
    #     listaCartas.append(valor) 
    
    # for i in range(5):
    #     carta = MiCarta(listaCartas[i])
    #     carta.dibujacarta(carta)
        
    # print(listaCartas)    
    
    
    
    # LIMPIO EL TERMINAL #
    clearTermina()
    
    
    # INICIAMOS EL JUEGO PIDIENDO MODO DE EJECUCION #
    print("Indique el modo de ejecucion:")
    modoEjecucion = input("[J]uego [A]nalisi:")
    
    bucle1 = False
    
    while bucle1 == False:
        if modoEjecucion == "J" or modoEjecucion == "j":
            bucle1 = True
            separaciones()
            print("### MODO JUEGO SELECCIONADO ###")
        
        elif modoEjecucion == "A" or modoEjecucion == "a":
            bucle1 = True
            separaciones()
            print("### MODO ANALISIS SELECCIONADO ###")
    
        elif modoEjecucion == "":
            bucle1 = True
            separaciones()
            print("### MODO JUEGO PREDETERMINADO ###")
        else:
            separaciones()
            print("Opcion insertada no valida, vuelva a insertar el modo de ejecucion")
            modoEjecucion = input("[J]uego [A]nalisi:")
    
    

if __name__ == "__main__":
    Main()
    
    
