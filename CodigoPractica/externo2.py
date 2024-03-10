import random

class CartaBase(object):
    """ Clase minimalista que representa una carta de la baraja
        Debería crearse una clase que herede de esta
    """
    def __init__(self, ind):
        """ Crea la carta con ese índice (0-51)
        :param ind: El índice de la carta
        """
        self.ind = ind

    @property
    def valor(self):
        """
        :return: Valor facial de la carta (1-10). Los ases devuelven 1.
        """
        return min(10, self.ind % 13 + 1)


class Estrategia(object):
    """ Clase que representa una estrategia de juego para el Blackjack
        Basada en el libro que muestra Alan en Resacón en las Vegas
    """
    # Matrices de estrategia: Filas suma de valores de cartas del jugador (ases = 1), columnas valor carta del croupier
    # Matriz para jugadas con 2 cartas del mismo valor (inicio fila 2)
    MATD = ['S' * 10, *['P' + 'S' * 6 + 'PPP'] * 2, 'P' * 4 + 'SS' + 'P' * 4, 'P' + 'D' * 8 + 'P',
            'P' + 'S' * 6 + 'PPP', 'P' + 'S' * 7 + 'PP', 'S' * 10, 'C' + 'S' * 5 + 'CSSC', 'C' * 10]
    # Matriz para jugadas con algún as (inicio fila 3, suma debe dividirse por 2)
    MATA = [*['P' * 4 + 'DD' + 'P' * 4] * 2, *['PPPDDD' + 'P' * 4] * 2, 'PP' + 'D' * 4 + 'P' * 4,
            'PC' + 'D' * 4 + 'CCPP', *['C' * 10] * 3]
    # Matriz para jugadas sin ases ni duplicados (inicio fila 4)
    MATN = [*['P' * 10] * 5, 'P' + 'D' * 5 + 'P' * 4, 'P' + 'D' * 8 + 'P', 'D' * 10,
            'P' * 3 + 'C' * 3 + 'P' * 4, *['P' + 'C' * 5 + 'P' * 4] * 4, *['C' * 10] * 5]
    # Vector de estrategia de conteo
    CONT = [-2, 2, 2, 2, 3, 2, 1, 0, -1, -2]

    def __init__(self, num_barajas):
        """ Crea e inicializa la estrategia
        :param num_barajas: Número de barajas del mazo utilizado en el juego
        """
        self.num_barajas = num_barajas
        self.num_cartas = 0
        self.cuenta = 0

    def cuenta_carta(self, carta):
        """ Este método se llama automáticamente por el objeto Mazo cada vez
            que se reparte una carta
        :param carta: La carta que se ha repartido
        """
        self.num_cartas += 1
        if self.num_cartas >= 52 * self.num_barajas:
            # Se ha cambiado el mazo
            self.num_cartas = 1
            self.cuenta = 0
        self.cuenta += Estrategia.CONT[carta.valor-1]

    def apuesta(self, apu_lo, apu_med, apu_hi):
        """ Indica la apuesta que se debe realizar dado el estado del juego.
            Elige entre 3 valores posibles (baja, media y alta)
        :param apu_lo: El valor de la apuesta baja
        :param apu_med: El valor de la apuesta media
        :param apu_hi: El valor de la apuesta alta
        :return: Uno de los 3 valores posibles de apuesta
        """
        barajas_restantes = self.num_barajas - self.num_cartas // 52
        true_count = self.cuenta / barajas_restantes
        if true_count > 1.0:
            return apu_hi
        elif true_count < -1.0:
            return apu_lo
        else:
            return apu_med

    def jugada(self, croupier, jugador):
        """ Indica la mejor opción dada la mano del croupier (que se supone que
            consta de una única carta) y la del jugador
        :param croupier: La carta del croupier
        :param jugador: La lista de cartas de la mano del jugador
        :return: La mejor opción: 'P' (pedir), 'D' (doblar), 'C' (cerrar) o 'S' (separar)
        """
        vc = croupier.valor
        vj = sum(c.valor for c in jugador)
        if len(jugador) == 2 and jugador[0].valor == jugador[1].valor:
            return Estrategia.MATD[vj//2 - 1][vc - 1]
        if any(c.valor == 1 for c in jugador) and vj < 12:
            return Estrategia.MATA[vj - 3][vc - 1]
        return Estrategia.MATN[vj - 4][vc - 1]



class Mazo(object):
    """ Clase que representa un mazo de cartas
    """
    NUM_BARAJAS = 2
    SEMILLA = 260

    def __init__(self, clase_carta, estrategia):
        """ Crea un mazo y le asocia una estrategia
        :param clase_carta: La clase que representa las cartas
        :param estrategia: La estrategia asociada
        """
        self.clase = clase_carta
        self.estrategia = estrategia
        self.cartas = []
        random.seed(Mazo.SEMILLA)

    def reparte(self):
        """ Reparte una carta del mazo
            Llama al método cuenta_carta de la estrategia asociada
        :return: Un objeto carta de la clase indicada en el constructor
        """
        if len(self.cartas) == 0:
            # Se ha acabado el mazo: crear uno nuevo
            inds = list(range(52)) * Mazo.NUM_BARAJAS
            random.shuffle(inds)
            self.cartas = [self.clase(i) for i in inds]
        c = self.cartas.pop()
        if self.estrategia is not None:
            # Se informa a la estrategia de la carta que se reparte
            self.estrategia.cuenta_carta(c)
        return c