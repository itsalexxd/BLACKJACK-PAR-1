"""
Practica 1 - Paradigmas de Programación
García Lavandera, Alejandro
García del Caz, Carla
Curso 2023-2024
"""

import externo2
'''
from externo import Mazo, Estrategia, CartaBase 
'''
import os

# Genero una baraja de cartas mezclada con 2 mazos
def generamosMazo():
    estrategia = externo2.Estrategia(externo2.Mazo.NUM_BARAJAS)
    mazo = externo2.Mazo(MiCarta,estrategia)

    listaCartas = []
    # Calculo e inserto el indice de las cartas en listaCartas
    for i in range(103):
        valor = int(mazo.reparte().ind)
        listaCartas.append(valor)

    return listaCartas

#PICAS TREBOLES DIAMANTES CORAZONES ♠  ♣  ♦  ♥
# A-10 y (J Q K) = 10
class MiCarta(externo2.CartaBase):
    # Devuelve el palo en un rango de 0-51
    @property
    def palo(self):
        if self.ind >= 0 and self.ind <= 12:
            return "♠"  # [PICAS]"
        elif self.ind >= 13 and self.ind <= 25:
            return "♣" # [TREBOLES]"
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
            if (carta % 13 + 1) in [11, 12, 13]:
                valor += 10
            elif (carta % 13 + 1) == 1:
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
        self.estado = "Pasada"

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
            print("╭────╮", end='\0')
            
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
                print("╰────╯", end='\0')

        def reiniciar_mano_croupier(self):
            self.mano = Mano("Croupier")



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
            
    def limpiar_manos (self):
        self.manos= []
        self.apuesta= []
        self.estado_mano = []
            
    def reiniciar_manos_jugador (self):
        self.limpiar_manos()


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
                print(" │ ", end='\0')
            print(f"<{self.nombre_mano[i]}>:", end='\0')
            for j in range (len(self.manos[i].cartas)):
                print("╭────╮", end='\0')
        
        
        print()
        
        
        # Linea 2
        # Mostramos el valor total de la mano y el valor de la/s carta/s
        for i in range(len(self.manos)):
            if i > 0:
                if self.calcular_valor_manos() < 10:
                    print(" │ ", end='\0')
                else:
                    print(" │ ", end='\0')
                    
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
                print(" │ ", end='\0')
                        
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
                print(" │ ", end='\0')
                        
            if self.estado_mano[i] == "Cerrada":
                print(f"{self.estado_mano[i]} ", end='\0')
            else:
                print(f" {self.estado_mano[i]} ", end='\0')
            for j in range(len(self.manos[i].cartas)):
                    print("╰────╯", end='\0')

            
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
        return "♣" # [TREBOLES]
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

###################
### MODO JUEGO ####
###################
def modoJuego(mazo):
    croupier = Croupier()       # Creo el croupier
    jugador = Jugador()     # Creo al jugador

    jugador.agregar_mano()      # Le doy una mano al jugador
    balance = 0     # Balance de la partida del jugador
    
    partida = True      # Variable para llevar el control del bucle de las partidas
    while partida:
        contador_partidas = 1       # Variable que lleva las cuentas de las partidas que lleva el jugador
        print("--- INICIO PARTIDA #", contador_partidas, " --- BALANCE = ", balance, "€")
        
        
        control_apuesta = True     # Variable para controlar el bucle a la hora de pedir la apuesta
        while control_apuesta:      # Bucle para controlar las excepciones a la hora de pedir el valor de la apuesta
            valor_apuesta_str = input("¿Apuesta? [2] [10] [50] ")       # Pido que inserte la apuesta que desea realizar
            valor_apuesta = int(valor_apuesta_str)      # Transformo el valor en int
            
            if valor_apuesta not in [2,10,50]:      # Si la apuesta no coincide con los valores validos, muestro mensaje de error por pantalla
                print("El valor insertado no es valido, inserte un valor correcto")
            
            else:       # La apuesta es correcta, empieza el reparto inicial
                control_apuesta = False      # Cambiamos el estado de la variable que controla el bucle para que no vuelva a pedirnos la apuesta
                jugador.apuesta.append(valor_apuesta)       # Guardamos la apuesta en la clase del jugador
        
        separaciones(2)
        
        #########################
        #### REPARTO INICIAL ####
        #########################
        print("REPARTO INICIAL")
        # Inserto una carta al croupier y al jugador
        '''
        dos cartas al jugador
        '''
        croupier.mano.agregar_carta(mazo.pop())
        jugador.agregar_carta_jugador(0, mazo.pop())        # El 0 hace referencia a la mano inicial del jugador
        
        imprimeInfo(croupier, jugador)      # Mostramos la informacion de las manos del croupier y del jugador
        
        ###########################
        #### TURNO DEL JUGADOR ####
        ###########################
        print("TURNO DEL JUGADOR")
        control_jugador = True      # Variable que lleva el control del bucle del jugador
        manos_cerradas = 0      # Variable que lleva la cuenta de las manos cerradas y pasadas (no se pueden modificar)
        while control_jugador:      # Bucle para llevar a cabo el turno del jugador para cada mano
            for i in range(len(jugador.manos)):     # Recorro todas las manos del jugador
                if jugador.estado_mano[i] in ["Cerrada", "Pasada"]:     # En este caso, el jugador no podra gestionar la mano en cuestion y lo mostramos por pantalla
                    print(f"La mano {jugador.nombre_mano[i]} esta {jugador.estado_mano[i]} y no puede ser modificada.")
                
                else:       # En este caso la mano esta abierta y puede ser modificada
                    control_jugada = True      # Variable que lleva el control del bucle para las jugadas del jugador y tratar los errores
                    while control_jugada:
                        if compara_cartas(jugador, i) == False:     # En caso de que no haya dos cartas con el mismo valor(Ej: 7 y 7), no se muestra la opcion para separar la mano
                            jugada = input(f"¿Jugada para {jugador.nombre_mano[i]}? [P]edir [D]oblar [C]errar ")        # Pido al jugador que inserte la jugada que desea realizar
                            
                            if jugada not in ["P", "p", "C", "c", "D", "d"]:        # Si la jugada insertada no es valida, mostramos el error por pantalla y lo volvemos a pedir
                                print(f"Entrada no valida, por favor, inserte de nuevo la jugada que desea realizar para la {jugador.nombre_mano[i]}")
                            
                        else:
                            jugada = input(f"¿Jugada para {jugador.nombre_mano[i]}? [P]edir [D]oblar [C]errar [S]eparar ")        # Pido al jugador que inserte la jugada que desea realizar
                            
                            if jugada not in ["P", "p", "C", "c", "D", "d", "S", "s"]:        # Si la jugada insertada no es valida, mostramos el error por pantalla y lo volvemos a pedir
                                print(f"Entrada no valida, por favor, inserte de nuevo la jugada que desea realizar para la {jugador.nombre_mano[i]}")
                        control_jugada = False      # Salimos del bucle
                        
                    if jugada in ["P", "p"]:        # Pedimos y agregamos una carta a la mano en cuestion
                        jugador.agregar_carta_jugador(i, mazo.pop())        # i hace referencia a la mano, mazo.pop() inserta una carta del mazo
                    
                    elif jugada in ["D", "d"]:      # Doblamos la apuesta del jugador, agregamos una carta y cambiamos el estado de la mano correspondiente
                        jugador.apuesta[i] = jugador.apuesta[i] * 2        # Doblamos la apuesta de la mano correspondiente
                        jugador.agregar_carta_jugador(i, mazo.pop())        # Agregamos una carta a la mano correspondiente
                        
                        if jugador.calcular_valor_mano(i) > 21:     # Si el valor total de la mano es valor > 21 -> PASADA
                            jugador.estado_mano[i] = "Pasada"
                            manos_cerradas += 1     # Sumamos 1 a las manos cerradas / pasadas

                        else:       # valor < 21 -> Cerrada
                            jugador.estado_mano[i] = "Cerrada"
                            manos_cerradas += 1     # Sumamos 1 a las manos cerradas / pasadas
                    
                    elif jugada in ["C", "c"]:      # jugada insertada = "C" o "c"
                        jugador.estado_mano[i] = "Cerrada"      # Cambiamos el estado de la mano a Cerrada
                        manos_cerradas += 1     # Sumamos 1 a las manos cerradas / pasadas
                    
                    else:    #Caso separar: Separar
                        jugador.separarMano(i, dime_carta_repetida(jugador, i))     # Separamos la mano cuando haya 2 cartas con el mismo valor (Ej: 7 y 7)
                    
                    
                
            if manos_cerradas == len(jugador.manos):
                jugador.imprime_jugador()
                control_jugador = False
            else:
                jugador.imprime_jugador()
        
        separaciones(2)
        
        ############################
        #### TURNO DEL CROUPIER ####
        ############################
        print("TURNO DEL CROUPIER")
        
        croupier.imprime_croupier()
        
        print()
        
        while croupier.mano.calcular_valor() < 17:
            croupier.mano.agregar_carta(mazo.pop())
            print()
            croupier.imprime_croupier()
        
        separaciones(3)
        
        
        ##################
        #### RECUENTO ####
        ##################
        
        
        ###########################
        #### FIN DE LA PARTIDA ####
        ###########################
        volver_jugar = True
        while volver_jugar:
            otra_partida = input(print("¿Otra partida? [S/N] "))    # Variable para la respuesta de jugar otra partida
            if otra_partida in ["S", "s"]:      # Se juega otra partida (no hacemos nada, el bucle empieza de nuevo)
                contador_partidas += 1      # Sumamos una partida a la variable
                volver_jugar = False
            
            elif otra_partida in ["N", "n"]:        # Mostramos el balance final y cerramos el bucle
                print("BALANCE FINAL: ", balance, "€")
                volver_jugar = False
                partida = False
                
            else:       # Entrada no valida, la pedimos de nuevo
                print("Entrada no valida, por favor, insertela de nuevo")
                
                
        

#######################
#### MODO ANÁLISIS ####
######################
def modoAnalisis(mazo):
    croupier = Croupier() #Creo al croupier
    jugador = Jugador()   #Creo al jugador
    jugador.agregar_mano() #Creo una mano al jugador
    balance = 0
    estrategia = externo2.Estrategia(externo2.Mazo.NUM_BARAJAS) #Crear la estrategia que el mº de barajas que hay en el mazo
    partidas=int(input("¿Número de partidas?"))
    
    for i in range (partidas):
        print("--- INICIO PARTIDA #", i+1, " --- BALANCE = ", balance, "€")
        croupier.reiniciar_mano_croupier()
        jugador.reiniciar_manos_jugador() #Reinicio las manos del croupier y del jugador cada vez que se empiece una partida
        
        croupier.mano.agregar_carta(mazo.pop()) #Agregar una mano al croupier y dos cartas al jugador
        for _ in range(2):
            jugador.agregar_carta_jugador(0, mazo.pop())
            
        apuesta = estrategia.apuesta(2,10,50) #Calcular la apuesta según la estrategia
        print ("¿Apuesta? [2] [10] [50] ", apuesta)
        
        separaciones(2)
        
        print("REPARTO INICIAL")
        imprimeInfo(croupier, jugador)
        
        ###########################
        #### TURNO DEL JUGADOR ####
        ###########################
        print("TURNO DEL JUGADOR")
        control_jugador = True
        manos_cerradas = 0
        manos_pasadas = 0
        
        while control_jugador:
            for j in range (len(jugador.manos)):
                mano_actual = jugador.manos[j]
                
                if jugador.estado_mano[j] in ["Cerrada", "Pasada"]:
                    print(f"La mano {jugador.nombre_mano[j]} esta {jugador.estado_mano[j]} y no puede ser modificada.")
                    
                else:
                    if compara_cartas(jugador, j) == False:
                        print (f"¿Jugada para {jugador.nombre_mano[j]}? [P]edir [D]oblar [C]errar ")
                        jugada = estrategia.jugada(croupier.mano.cartas[0], mano_actual.cartas)
                        jugada = jugada.upper()
                            
                        if jugada == "S":
                            print ("No se pueden separar las cartas")
                                
                    else:
                        print (f"¿Jugada para {jugador.nombre_mano[j]}? [P]edir [D]oblar [C]errar [S]eparar")
                    
                    if jugada == "P":
                        jugador.agregar_carta_jugador(j,mazo.pop())
                        
                    elif jugada == "D":
                        jugador.apuesta[j] *= 2
                        jugador.agregar_carta_jugador(j, mazo.pop())
                        
                        if jugador.calcular_valor_mano(j) > 21:
                            jugador.estado_mano[j] = "Pasada"
                            manos_cerradas += 1
                            manos_pasadas +=1
                            
                        else:
                            jugador.estado_mano[j] = "Cerrada"
                            manos_cerradas += 1
                
                    elif jugada == "C":
                        jugador.estado_mano[j] = "Cerrada"
                        manos_cerradas += 1
                        
                    elif jugada == "S":
                        jugador.separarMano(j, dime_carta_repetida(jugador, j))
                        
        if manos_cerradas == len(jugador.manos):
            jugador.imprime_jugador()
            control_jugador = False
            
        else:
            jugador.imprime_jugador()
            
    separaciones (2)
    
    ############################
    #### TURNO DEL CROUPIER ####
    ############################
    print("TURNO DEL CROUPIER")
    croupier.imprime_croupier()
    print()
    
    if manos_pasadas == len(jugador.manos):
        croupier.imprime_croupier()
        
    else:
        while croupier.mano.calcular_valor() < 17:
            croupier.mano.agregar_carta(mazo.pop())
            print()
            croupier.imprime_croupier()
            
    if croupier.mano.calcular_valor()>21:
        croupier.mano.estado= "Pasada"
    
    else:
        croupier.mano.estado = "Cerrada"
        
    separaciones(3)
    
    ##################
    #### RECUENTO ####
    ##################


def modoPredeterminado(mazo):
    croupier= Croupier()
    jugador = Jugador()
    
    jugador.agregar_mano()
    balance = 0
    
    partida = True
    while partida:
        contador_partidas = 1
        print("--- INICIO PARTIDA #", contador_partidas, " --- BALANCE = ", balance, "€")
        
        apuesta = 10
        print ("¿Apuesta? [2] [10] [50] ")
        
    separaciones(2)
    
    #########################
    #### REPARTO INICIAL ####
    #########################
    print("REPARTO INICIAL")
    
    croupier.mano.agregar_carta(mazo.pop()) #Agregar una mano al croupier y dos cartas al jugador
    for _ in range(2):
        jugador.agregar_carta_jugador(0, mazo.pop())
        
    imprimeInfo(croupier, jugador)
    
    ###########################
    #### TURNO DEL JUGADOR ####
    ###########################
    print("TURNO DEL JUGADOR")
    control_jugador = True      # Variable que lleva el control del bucle del jugador
    manos_cerradas = 0      # Variable que lleva la cuenta de las manos cerradas y pasadas (no se pueden modificar)
    while control_jugador:      # Bucle para llevar a cabo el turno del jugador para cada mano
        for i in range(len(jugador.manos)):     # Recorro todas las manos del jugador
            if jugador.estado_mano[i] in ["Cerrada", "Pasada"]:     # En este caso, el jugador no podra gestionar la mano en cuestion y lo mostramos por pantalla
                print(f"La mano {jugador.nombre_mano[i]} esta {jugador.estado_mano[i]} y no puede ser modificada.")
            
            else:       # En este caso la mano esta abierta y puede ser modificada
                control_jugada = True      # Variable que lleva el control del bucle para las jugadas del jugador y tratar los errores
                while control_jugada:
                    if compara_cartas(jugador, i) == False:     # En caso de que no haya dos cartas con el mismo valor(Ej: 7 y 7), no se muestra la opcion para separar la mano
                        jugada = input(f"¿Jugada para {jugador.nombre_mano[i]}? [P]edir [D]oblar [C]errar ")        # Pido al jugador que inserte la jugada que desea realizar
                        
                        if jugada not in ["P", "p", "C", "c", "D", "d"]:        # Si la jugada insertada no es valida, mostramos el error por pantalla y lo volvemos a pedir
                            print(f"Entrada no valida, por favor, inserte de nuevo la jugada que desea realizar para la {jugador.nombre_mano[i]}")
                        
                    else:
                        jugada = input(f"¿Jugada para {jugador.nombre_mano[i]}? [P]edir [D]oblar [C]errar [S]eparar ")        # Pido al jugador que inserte la jugada que desea realizar
                        
                        if jugada not in ["P", "p", "C", "c", "D", "d", "S", "s"]:        # Si la jugada insertada no es valida, mostramos el error por pantalla y lo volvemos a pedir
                            print(f"Entrada no valida, por favor, inserte de nuevo la jugada que desea realizar para la {jugador.nombre_mano[i]}")
                    control_jugada = False      # Salimos del bucle
                    
                if jugada in ["P", "p"]:        # Pedimos y agregamos una carta a la mano en cuestion
                    jugador.agregar_carta_jugador(i, mazo.pop())        # i hace referencia a la mano, mazo.pop() inserta una carta del mazo
                
                elif jugada in ["D", "d"]:      # Doblamos la apuesta del jugador, agregamos una carta y cambiamos el estado de la mano correspondiente
                    jugador.apuesta[i] = jugador.apuesta[i] * 2        # Doblamos la apuesta de la mano correspondiente
                    jugador.agregar_carta_jugador(i, mazo.pop())        # Agregamos una carta a la mano correspondiente
                    
                    if jugador.calcular_valor_mano(i) > 21:     # Si el valor total de la mano es valor > 21 -> PASADA
                        jugador.estado_mano[i] = "Pasada"
                        manos_cerradas += 1     # Sumamos 1 a las manos cerradas / pasadas

                    else:       # valor < 21 -> Cerrada
                        jugador.estado_mano[i] = "Cerrada"
                        manos_cerradas += 1     # Sumamos 1 a las manos cerradas / pasadas
                
                elif jugada in ["C", "c"]:      # jugada insertada = "C" o "c"
                    jugador.estado_mano[i] = "Cerrada"      # Cambiamos el estado de la mano a Cerrada
                    manos_cerradas += 1     # Sumamos 1 a las manos cerradas / pasadas
                
                else:    #Caso separar: Separar
                    jugador.separarMano(i, dime_carta_repetida(jugador, i))     # Separamos la mano cuando haya 2 cartas con el mismo valor (Ej: 7 y 7)
                
                
            
        if manos_cerradas == len(jugador.manos):
            jugador.imprime_jugador()
            control_jugador = False
        else:
            jugador.imprime_jugador()
    
    separaciones(2)
    
    ############################
    #### TURNO DEL CROUPIER ####
    ############################
    print("TURNO DEL CROUPIER")
    
    croupier.imprime_croupier()
    
    print()
    
    while croupier.mano.calcular_valor() < 17:
        croupier.mano.agregar_carta(mazo.pop())
        print()
        croupier.imprime_croupier()
    
    separaciones(3)
    
    ##################
    #### RECUENTO ####
    ##################

    ###########################
    #### FIN DE LA PARTIDA ####
    ###########################





def clearTerminal():
    os.system('clear')
    
def separaciones(num):
    for i in range(num):
        print()
        

def Main():
    clearTerminal()
    
    print("*** BLACKJACK - PARADIGMAS DE PROGRAMACIÓN 2023/24 ***")
    
    # estrategia = externo2.Estrategia(externo2.Mazo.NUM_BARAJAS)
    # mazo2 = externo2.Mazo(MiCarta, estrategia)
    
    mazo = generamosMazo()

    print("Indique el modo de ejecucion:")
    modoEjecucion = input("[J]uego [A]nalisis: ")
    
    separaciones(2)
    
    modo_juego = True
    while modo_juego:
        if modoEjecucion in ["J", "j"]:
            modoJuego(mazo)
            modo_juego = False
            
        elif modoEjecucion in ["A", "a"]:
            modoAnalisis(mazo)
            modo_juego = False
            
        elif modoEjecucion == "":
            modoPredeterminado(mazo)
            modo_juego = False
        
        else:
            separaciones(2)
            print("Opcion insertada no valida, vuelva a insertar el modo de ejecucion")
            modoEjecucion = input("[J]uego [A]nalisis:" )


if __name__ == "__main__":
    Main()