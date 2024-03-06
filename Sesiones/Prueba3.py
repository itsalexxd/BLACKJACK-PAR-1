# Sesion 3 -> Tratamiento de ficheros

# Ejemplo de lectura de ficheros
'''

'''

def Main():
    # Apertura del fichero
    with open ('ejemplo.txt', 'r') as fichero:
        # Leer contenido del fichero
        contenido = fichero.read()
        print (contenido)

    

if __name__ == "__main__":
    Main()

    