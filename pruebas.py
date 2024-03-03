import random

def imprimir_carta(palo, valor):
    carta = f"""
╭───────╮
│       │
│   {valor}   │
│   {palo}   │
│       │
╰───────╯
"""
    print(carta)
    
    
    
    
# Indico los rangos para los valores random
rangoCartasInicio = 1
rangoCartasFinal = 13
rangoMazosInicio = 1
rangoMazosFinal = 4    

def random(rangoCartasInicio, rangoCartasFinal, rangoMazosInicio, rangoMazosFinal):
    randomCartas = random.randint (rangoCartasInicio, rangoCartasFinal)
    randomMazos = random.randint (rangoMazosInicio, rangoMazosFinal)
    
    return randomCartas, randomMazos

# Genero los valores de forma random dentro de los rangos indicados
randomCartas, randomMazos = random(rangoCartasInicio, rangoCartasFinal, rangoMazosInicio, rangoMazosFinal)


mazoPicas = ['1','2','3','4','5','6','7','8','9','10','J','Q','K']
mazoTrevoles = ['1','2','3','4','5','6','7','8','9','10','J','Q','K']
mazoDiamantes = ['1','2','3','4','5','6','7','8','9','10','J','Q','K']
mazoCorazones = ['1','2','3','4','5','6','7','8','9','10','J','Q','K']
    
manoCoupier = []
manoJugador = []
    
    
def reparteCoupier(randomCartas, randomMazos, mazoPicas, mazoTrevoles, mazoCorazones, manoCoupier):
    

def recuperaCartas():
    cartasMazo = ['1','2','3','4','5','6','7','8','9','10','J','Q','K']
    longitud = len(cartasMazo)
    
    for cartas in range longitud:
           mazoCorazones.append(0)


if __name__ == "__main__":
    
