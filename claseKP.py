apuestaCorrecta = False
while apuestaCorrecta == False:
    valor_apuesta = int(input("Apuesta: "))
    if valor_apuesta == 2 or valor_apuesta == 10 or valor_apuesta == 50:
        print(valor_apuesta)
    else:
        print("No valida")
