import random

def imprimir_carta(palo, valor):
    carta = f"""
╭───────╮
│       │
│  {valor}   │
│   {palo}   │
│       │
╰───────╯
"""
    print(carta)
    



# Funcion para generar dos numeros aleatorios dentro de unos rangos indicados
def randomizador(rangoCartasInicio, rangoCartasFinal, rangoMazosInicio, rangoMazosFinal):
    randomCartas = random.randint(rangoCartasInicio, rangoCartasFinal)
    randomMazos = random.randint(rangoMazosInicio, rangoMazosFinal)
    
    return randomCartas, randomMazos

# Recupero el valor de las cartas en la baraja
def recuperaCartas():
    cartasMazo = ['1','2','3','4','5','6','7','8','9','10','J','Q','K']
    long = len(cartasMazo)
    
    for i in range (long):
        # Recorro el array con los valores de las cartas para guardarlo en la variable "restaurador"
        restaurador = cartasMazo.append(i)
        # Inserto el valor de la variable restaurador en las arrays
        mazoPicas.append(i, restaurador)
        mazoTrevoles.append(i, restaurador)
        mazoDiamantes.append(i, restaurador)
        mazoCorazones.append(i, restaurador)

# Funcion para mostrar la baraja completa
def muestraBaraja(baraja):
    for i, mazo in enumerate(baraja):
        print(f"Mazo {i + 1}: ", end="")
        print(*mazo, sep=", ")
        
class Mano:
    def __init__(self):
        self.cartas = []
        
    def agregarCartas(self, carta):
        self.cartas.append(carta)
        
    def obtenerSuma(self):
        valorTotal = 0
        ases = 0
        for carta in self.cartas:
            if carta in ['J', 'Q', 'K']:
                valorTotal += 10
            elif carta == 'A':
                ases += 1
            else:
                valorTotal += int(carta)
        
        for _ in range(ases):
            if valorTotal + 11 <= 21:
                valorTotal += 11
            else:
                valorTotal += 1
        
        return valorTotal

class Croupier:
    def __init__(self):
        self.mano = Mano()

class Jugador:
    def __init__(self):
        self.manos = [Mano()]
    
    
    
    
if __name__ == "__main__":
    
    # Indico los rangos para generar los valores random
    rangoCartasInicio = 1
    rangoCartasFinal = 13
    rangoMazosInicio = 1
    rangoMazosFinal = 4  
    # Genero 2 numeros de forma aleatoria para elegir mazo y carta
    randomCartas, randomMazos = randomizador(rangoCartasInicio, rangoCartasFinal, rangoMazosInicio, rangoMazosFinal)
    print (randomCartas, randomMazos)
    

    # Creo la baraja
    mazoPicas = ['1','2','3','4','5','6','7','8','9','10','J','Q','K']
    mazoTrevoles = ['1','2','3','4','5','6','7','8','9','10','J','Q','K']
    mazoDiamantes = ['1','2','3','4','5','6','7','8','9','10','J','Q','K']
    mazoCorazones = ['1','2','3','4','5','6','7','8','9','10','J','Q','K']
    baraja = [mazoPicas, mazoTrevoles, mazoDiamantes, mazoCorazones]
    
    muestraBaraja(baraja)
    imprimir_carta("♦", " J")
    imprimir_carta("♦", "10")    
    
    croupier = Croupier()
    jugador = Jugador()
    
    # Agregamos cartas
    croupier.mano.agregarCartas('J')
    jugador.manos[0].agregarCartas('5')
    
    # Mostramos el valor total
    print("Valor total de la mano del croupier:", croupier.mano.obtenerSuma())
    print("Valor total de la mano del jugador:", jugador.manos[0].obtenerSuma())