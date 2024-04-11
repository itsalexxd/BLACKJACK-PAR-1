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
            

####################
#### CLASE MANO ####
####################

class Mano:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cartas = []  # Inicializamos el atributo cartas como una lista vacía
        self.estado = "Activa"

    def agregar_carta(self, carta):
        self.cartas.append(carta)

    # Calcula el valor total de la mano
    def calcular_valor(self):
        # Inicializamos el valor en 0 antes de calcularlo nuevamente
        valor = 0
        num_as = 0  # Contador de ases (que valen 1 u 11)
        
        for carta in self.cartas:
            if carta % 13 + 1 in [11, 12, 13]:
                valor += 10
            elif carta % 13 + 1 == 1:
                num_as += 1
                valor += 11  # Asumimos el valor del as como 11 por defecto
            else:
                valor += int(carta % 13 + 1)  # Las cartas numéricas tienen su valor numérico
        
        # Ajustamos el valor de los ases si el total es mayor a 21
        while num_as > 0 and valor > 21:
            valor -= 10  # Restamos 10 al valor total por cada as
            num_as -= 1

        return valor
        
    # Traduce el indice de la carta en la baraja a la carta que es (Ej ind = 11 -> Q)
    def calcula_carta(self):
        for ind in self.cartas:
            if ind % 13 + 1 == 1:
                return "A"
            elif ind % 13 + 1 == 11:
                return "J"
            elif ind % 13 + 1 == 12:
                return "Q"
            elif ind % 13 + 1 == 13:
                return "K"
            else:
                return int(ind % 13 + 1)
            
    def traducir_carta(self, i):
        carta = self.cartas[i]
        return traduce_carta(carta)
        
    
    def traducir_palo(self, i):
        palo = self.cartas[i]
        return traduce_palo(palo)

    def abrir_mano(self):
        self.estado = "Activa"

    def cerrar_mano(self):
        self.estado = "Cerrada"
        
    def mano_pasada(self):
        self.estado = "PASADA"

########################
#### CLASE CROUPIER ####
########################

class Croupier():
    def __init__(self):
        self.croupier = "Croupier"
        self.mano = Mano("Croupier")
        
    def imprime_croupier(self):
        # Mostramos la primera parte: el nombre y la prate superior de la/s carta/s
        print(f"{self.croupier}:", end='\0')
        for i in range (len(self.mano.cartas)):
            print(f"╭────╮", end='\0')
            
        print()
        
        if self.mano.calcular_valor() < 10:
            print(f"     ({self.mano.calcular_valor()}) ", end='\0')
        else:
            print(f"    ({self.mano.calcular_valor()}) ", end='\0')
        for i in range(len(self.mano.cartas)):
                # La carta es != 10
                if self.mano.traducir_carta(i) != 10:
                    print(f"│   {self.mano.traducir_carta(i)}│", end='\0')
                # La carta es == 10
                else:
                    print(f"│  {self.mano.traducir_carta(i)}│", end='\0')
                    
        print()

        if self.mano.estado == "Activa":
            print(f"  {self.mano.estado} ", end='\0')
        elif self.mano.estado == "Cerrada":
            print(f"{self.mano.estado}", end='\0')
        else:
            print(f"  {self.mano.estado} ", end='\0')
        
        for i in range(len(self.mano.cartas)):
            print(f"│{self.mano.traducir_palo(i)}   │", end='\0')
        
        print()
        
        print("         ", end='\0')
        for i in range(len(self.mano.cartas)):
                    print(f"╰────╯", end='\0')




#######################
#### CLASE JUGADOR ####
#######################

class Jugador(Mano):
    def __init__(self):
        self.nombre = "Jugador"
        self.manos = []
        self.valor_mano = []
        self.apuesta = []
        self.nombre_mano = ["ManoA"]
        self.estado_mano = ["Activa"]
        
    def agregar_mano(self):
        nombreMano = f"Mano{chr(ord('A') + len(self.manos)+1)}"
        nuevaMano = Mano(nombreMano)
        self.manos.append(nuevaMano)
        self.nombre_mano.append(nombreMano)
        
    def obtener_mano(self, indice):
        return self.manos[indice]
    
    def agregar_carta_jugador(self, mano_indice, carta):
        if 0 <= mano_indice < len(self.manos):
            self.manos[mano_indice].agregar_carta(carta)
        else:
            print("El indice insertado para la mano no es valido")


    def calcular_valor_mano(self, indice_mano):
            # Inicializamos el valor en 0 antes de calcularlo nuevamente
            valor = 0 # Valor total de la mano
            num_as = 0  # Contador de ases (que valen 1 u 11)
            
            for j in range(len(self.manos[indice_mano].cartas)):
                if (self.manos[indice_mano].cartas[j] % 13 + 1) in [11, 12, 13]:
                    valor += 10
                elif (self.manos[indice_mano].cartas[j] % 13 + 1) == 1:
                    num_as += 1
                    valor += 11  # Asumimos el valor del as como 11 por defecto
                else:
                    valor += int(self.manos[indice_mano].cartas[j] % 13 + 1)  # Las cartas numéricas tienen su valor numérico
            
            # Ajustamos el valor de los ases si el total es mayor a 21
            while num_as > 0 and valor > 21:
                valor -= 10  # Restamos 10 al valor total por cada as
                num_as -= 1

            return valor
        
    def calcular_valor_mano_dos(self, indice_mano):
            # Inicializamos el valor en 0 antes de calcularlo nuevamente
            valor = 0 # Valor total de la mano
            num_as = 0  # Contador de ases (que valen 1 u 11)
            
            for j in range(len(self.manos[indice_mano].cartas)):
                if (self.manos[indice_mano].cartas[j] % 13 + 1) in [11, 12, 13]:
                    valor += 10
                elif (self.manos[indice_mano].cartas[j] % 13 + 1) == 1:
                    num_as += 1
                    valor += 11  # Asumimos el valor del as como 11 por defecto
                else:
                    valor += int(self.manos[indice_mano].cartas[j] % 13 + 1)  # Las cartas numéricas tienen su valor numérico
            
            # Ajustamos el valor de los ases si el total es mayor a 21
            while num_as > 0 and valor > 21:
                valor -= 10  # Restamos 10 al valor total por cada as
                num_as -= 1

            return str(valor)
        
        
    def calcular_valor_manos(self):
        for i in range(len(self.manos)):
            # Inicializamos el valor en 0 antes de calcularlo nuevamente
            valor = 0 # Valor total de la mano
            num_as = 0  # Contador de ases (que valen 1 u 11)
            
            for j in range(len(self.manos[i].cartas)):
                if (self.manos[i].cartas[j] % 13 + 1) in [11, 12, 13]:
                    valor += 10
                elif (self.manos[i].cartas[j] % 13 + 1) == 1:
                    num_as += 1
                    valor += 11  # Asumimos el valor del as como 11 por defecto
                else:
                    valor += int(self.manos[i].cartas[j] % 13 + 1)  # Las cartas numéricas tienen su valor numérico
            
            # Ajustamos el valor de los ases si el total es mayor a 21
            while num_as > 0 and valor > 21:
                valor -= 10  # Restamos 10 al valor total por cada as
                num_as -= 1
            
            return valor
    
    # Recibe el indice de la carta y traduce el indice al valor de la carta en cuestion
    def traducir_carta(self, i, j):
        carta = self.manos[i].cartas[j]
        return traduce_carta(carta)
    
    # Recibe el indice de la carta y lo traduce al palo correspondiente
    def traducir_palo(self, i, j):
        palo = self.manos[i].cartas[j]
        return traduce_palo(palo)
    
    # Muestra la informacion del jugador
    def imprime_jugador(self):
        # Linea 1
        # Mostramos el nombre de la mano y la parte superior
        for i in range(len(self.manos)):
            if i > 0:
                print(" | ", end='\0')
            print(f"<{self.nombre_mano[i]}>:", end='\0')
            for j in range (len(self.manos[i].cartas)):
                print(f"╭────╮", end='\0')
            
            
        print()
        
        
        # Linea 2
        # Mostramos el valor total de la mano y el valor de la/s carta/s
        for i in range(len(self.manos)):
            if i > 0:
                if self.calcular_valor_manos() < 10:
                    print(" |   ", end='\0')
                else:
                    print(" | ", end='\0')
                    
            if self.calcular_valor_mano(i) < 10:
                print(f"    ({self.calcular_valor_mano(i)}) ", end='\0')
            else:
                print(f"   ({self.calcular_valor_mano_dos(i)}) ", end='\0')
            for j in range (len(self.manos[i].cartas)):
                # La carta es != 10
                if self.traducir_carta(i,j) != 10:
                    print(f"│   {self.traducir_carta(i,j)}│", end='\0')
                # La carta es == 10
                else:
                    print(f"│  {self.traducir_carta(i,j)}│", end='\0')
                    
        
        
        print()
        
        # Linea 3
        # Mostramos la apuesta relacionada a la mano y el palo de la/s carta/s
        for i in range(len(self.manos)):
            if i > 0:
                print(" | ", end='\0')
                        
            if self.apuesta[i] < 10: # Ajustamos la apuesta en funcion del valor
                print(f"     {self.apuesta[i]}€ ", end='\0')
            else:
                print(f"    {self.apuesta[i]}€ ", end='\0')
            for j in range(len(self.manos[i].cartas)):
                print(f"│{self.traducir_palo(i,j)}   │", end='\0')
                    
        print()
        
        # Linea 4
        # Mostramos el estado de la mano y el final de la carta
        for i in range(len(self.manos)):
            if i > 0:
                print(" | ", end='\0')
                        
            if self.estado_mano[i] == "Cerrada":
                print(f"{self.estado_mano[i]} ", end='\0')
            else:
                print(f" {self.estado_mano[i]} ", end='\0')
            for j in range(len(self.manos[i].cartas)):
                    print(f"╰────╯", end='\0')

            
        separaciones(3)
                    
    # Separa la mano
    def separarMano(self, indice_mano, indice_carta):
        mano_original = self.manos[indice_mano]
        carta = mano_original.cartas.pop(indice_carta)  # Quitamos la carta de la mano original
        nombre_nueva_mano = f"{mano_original.nombre}{chr(ord('A') + len(self.manos) - 1)}"
        nueva_mano = Mano(nombre_nueva_mano)  # Creamos una nueva mano para la carta separada
        nueva_mano.agregar_carta(carta)  # Agregamos la carta separada a la nueva mano
        self.manos.append(nueva_mano)  # Agregamos la nueva mano a las manos del jugador
        self.apuesta.append(self.apuesta[indice_mano])
        self.estado_mano.append("Activa")

# Recibe el indice de una carta y calcula el valor de la carta correspondiente al indice
def traduce_carta(carta):
    if carta % 13 + 1 == 1:
        return "A"
    elif carta % 13 + 1 == 11:
        return "J"
    elif carta % 13 + 1 == 12:
        return "Q"
    elif carta % 13 + 1 == 13:
        return "K"
    else:
        return carta % 13 + 1
    
# Recibe el indice de una carta y calcula el palo de la carta correspondiente al indice
def traduce_palo(palo):
    if palo >= 0 and palo <= 12:
        return "♠"  # [PICAS]
    elif palo >= 13 and palo <= 25:
        return "♣" # [TREVOLES]
    elif palo >= 26 and palo <= 38:
        return "♦" # [DIAMANTES]
    else:
        return "♥" # [CORAZONES]

# Imprime la informacion del Croupier y Jugador
def imprimeInfo(croupier, jugador):
    croupier.imprime_croupier()
    print('\n')
    jugador.imprime_jugador()

# Compara las cartas de la mano[i] del jugador
    # 2 cartas iguales -> True
    # No hay cartas iguales -> False
def compara_cartas(jugador, i):
    # Variable para ver si hay cartas iguales
    cartas_iguales = 0
    # Si hay mas de una carta en la mano, comprobamos si hay 2 cartas iguales
    if len(jugador.manos[i].cartas) > 1:
        for j in range(len(jugador.manos[i].cartas) - 1): # Recorro las cartas (carta que comparo)
            carta1 = jugador.manos[i].cartas[j] # Guardo el indice de la carta en carta1 (la que comparamos)
            carta =  traduce_carta(carta1) # Traducimos el indice en el valor de la carta
            for q in range(len(jugador.manos[i].cartas)): # Recorro las cartas (carta que uso para comparar)
                carta2 = jugador.manos[i].cartas[q] # Guardo el indice de la carta en carta2 (con la que se compara)
                otra_carta = traduce_carta(carta2) # Traducimos el indice en el valor de la carta
            
            # Compruebo si las cartas son iguales o no (no pueden valer lo mismo j y q (es la misma carta))
            if j != q and carta == otra_carta:
                # Si carta == otra_carta, sumamos 1 a la variable ya que tienen el mismo valor de carta
                cartas_iguales += 1
                
        if cartas_iguales > 0:
            return True
        else:
            return False
    # Si solo hay una carta, devolvemos FALSE automaticamente ya que no puede haber otra carta igual
    else:
        return False

def dime_carta_repetida(jugador, i):
    # Variable para ver si hay cartas iguales
    cartas_iguales = 0
    # Si hay mas de una carta en la mano, comprobamos si hay 2 cartas iguales
    if len(jugador.manos[i].cartas) > 1:
        for j in range(len(jugador.manos[i].cartas) - 1): # Recorro las cartas (carta que comparo)
            carta1 = jugador.manos[i].cartas[j] # Guardo el indice de la carta en carta1 (la que comparamos)
            carta =  traduce_carta(carta1) # Traducimos el indice en el valor de la carta
            for q in range(len(jugador.manos[i].cartas)): # Recorro las cartas (carta que uso para comparar)
                carta2 = jugador.manos[i].cartas[q] # Guardo el indice de la carta en carta2 (con la que se compara)
                otra_carta = traduce_carta(carta2) # Traducimos el indice en el valor de la carta
            
            # Compruebo si las cartas son iguales o no (no pueden valer lo mismo j y q (es la misma carta))
            if j != q and carta == otra_carta:
                # Si carta == otra_carta, sumamos 1 a la variable ya que tienen el mismo valor de carta
                return q
    
def modoJuego(mazo):
    # Variable que controla el bucle para jugar partidas
    finPartidas = True
    # Contador del balance del jugador y las apuestas
    balance = 0
    
    while finPartidas:
        # Contador de partidas
        contador_partidas = 1
        # Creo al croupier y al jugador
        croupier = Croupier()
        jugador = Jugador()
        
        print("--- INICIO PARTIDA #", contador_partidas, " --- BALANCE = ", balance, "€" )
        
        separaciones(2)

        apuesta_correcta = False
        while apuesta_correcta == False:
            valorApuesta = int(input("¿Apuesta? [2] [10] [50]  "))
            if valorApuesta in [2, 10, 50]:
                jugador.apuesta.append(valorApuesta)
                
                # Agregamos una mano al jugador
                jugador.agregar_mano()
                
                separaciones(2)

                print("REPARTO INICIAL")
                # Inserto la primera carta al croupier y al jugador
                croupier.mano.agregar_carta(mazo.pop())
                jugador.agregar_carta_jugador(0,mazo.pop())
                
                # Muestra la informacion del croupier y el jugador
                imprimeInfo(croupier, jugador)
                
                # Turno del jugador
                print("TURNO DEL JUGADOR")
                fin_jugador = False
                
                while fin_jugador == False:
                    for i in range(len(jugador.manos)): # Recorro las manos del jugador
                        if jugador.estado_mano[i] == "Activa": # Si el estado de la mano no es Activa, no se podra editar
                            if compara_cartas(jugador, i) == False: # Compruebo si se activa la funcion para separar y mostrarla
                                jugada = input(f"¿Jugada para {jugador.nombre_mano[i]}? [P]edir [D]oblar [C]errar  ")
                                
                                # Pedimos carta (agregamos carta a la mano i)
                                if jugada == "P" or jugada == "p":
                                    jugador.agregar_carta_jugador(i, mazo.pop())
                                    
                                
                                # Cerramos la mano i
                                elif jugada in ["C", "c"]:
                                    jugador.estado_mano[i] = "Cerrada"
                                
                                # Doblamos la apuesta de la mano i, sumamos una carta y si la suma > 21 -> PASADA; sino Cerrada
                                elif jugada in ["D", "d"]:
                                    jugador.apuesta[i] = jugador.apuesta[i] * 2 # Doblamos la apuesta
                                    jugador.agregar_carta_jugador(i, mazo.pop()) # Agregamos una carta
                                    if jugador.calcular_valor_mano(i) > 21: # Si el valor de la mano supera 21
                                        jugador.estado_mano[i] = "PASADA" # El estado pasa a ser PASADA
                                    else:
                                        jugador.estado_mano[i] = "Cerrada" # Si no, se cierra la mano
                                    
                                    
                                
                                # Entrada no valida
                                else:
                                    print("Entrada no valida, inserte de nuevo la accion que desea realizar...")
                                    jugada = input(f"¿Jugada para {jugador.nombre_mano[i]}? [P]edir [D]oblar [C]errar ")
                                    
                                    
                            # La opcion separar se activa ya que tiene 2 cartas con el mismo valor
                            else:
                                jugada = input(f"¿Jugada para {jugador.nombre_mano[i]}? [P]edir [D]oblar [C]errar [S]eparar  ")
                                # Pedimos carta (agregamos carta a la mano i)
                                if jugada == "P" or jugada == "p":
                                    jugador.agregar_carta_jugador(i, mazo.pop())
                                    
                                
                                # Cerramos la mano i
                                elif jugada in ["C", "c"]:
                                    jugador.estado_mano[i] = "Cerrada"
                                
                                # Doblamos la apuesta de la mano i, sumamos una carta y si la suma > 21 -> PASADA; sino Cerrada
                                elif jugada in ["D", "d"]:
                                    jugador.apuesta[i] = jugador.apuesta[i] * 2 # Doblamos la apuesta
                                    jugador.agregar_carta_jugador(i, mazo.pop()) # Agregamos una carta
                                    if jugador.calcular_valor_mano(i) > 21: # Si el valor de la mano supera 21
                                        jugador.estado_mano[i] = "PASADA" # El estado pasa a ser PASADA
                                    else:
                                        jugador.estado_mano[i] = "Cerrada" # Si no, se cierra la mano
                                        
                                # Separamos la mano ya que tiene 2 cartas con el mismo valor
                                elif jugada == "S" or jugada == "s":
                                    jugador.separarMano(i, dime_carta_repetida(jugador, i))
                                    
                                
                                # Enrtada no valida, la pedimos de nuevo
                                else:
                                    print("Entrada no valida, insertela de nuevo...")
                                    jugada = input(f"¿Jugada para {jugador.nombre_mano[i]}? [P]edir [D]oblar [C]errar [S]eparar  ")
                        # En caso de que el estado de la mano no sea Activo, no se podra modificar
                        else:
                            print(f"La mano {jugador.nombre_mano[i]} esta {jugador.estado_mano[i]}.")
                            i = i + 1
                            
                        print()
                        
                        jugador.imprime_jugador()
                    
                fin_jugador = True
                    
                    
                    
            else:
                print("Apuesta no valida, inserte la apuesta de nuevo...")
                valorApuesta = int(input("¿Apuesta? [2] [10] [50]  "))
        else:
            print("Apuesta no valida, inserte la apuesta de nuevo...")
            valorApuesta = int(input("¿Apuesta? [2] [10] [50]  "))
                
        contador_partidas += 1
        
        
        
        
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
    
    separaciones(2)
    
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