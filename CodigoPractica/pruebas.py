import externo2

class MiCarta(externo2.CartaBase):
    def __init__(self, ind, palo):
        self.palo = palo


    # Devuelve el palo en un rango de 0-51
    def palo(self):
        if self.ind >= 0 and self.ind <= 12:
            return "♠"
        elif self.ind >= 13 and self.ind <= 25:
            return "♣"
        elif self.ind >= 26 and self.ind <= 38:
            return "♦"
        else:
            return "♥"
            


#################
#### M A I N ####
#################

def Main():
    pass


if __name__ == "__main__":
    Main()
    
    
# PICAS TREVOLES DIAMANTES CORAZONES ♠  ♥  ♦  ♣#