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

# Ejemplo de uso
imprimir_carta("♥", "J")