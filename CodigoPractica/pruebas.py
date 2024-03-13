import externo2

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
    
def dibujacarta(carta):
    if(carta.valor) == 10:
        carta = f"""
╭───────╮
│       │
│    {carta.valor} │
│       │
│  {carta.palo}    │
│       │
╰───────╯
    """
    else:
        carta = f"""
╭───────╮
│       │
│    {carta.valor}  │
│       │
│  {carta.palo}    │
│       │
╰───────╯
    """
    print(carta)


#################
#### M A I N ####
#################

def Main():
    carta = MiCarta(35)
    dibujacarta(carta)
    


if __name__ == "__main__":
    Main()
    
    
