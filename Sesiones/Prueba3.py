# Sesion 3 -> Tratamiento de ficheros y excepciones

# Como importar paquetes externos en python
'''
IMPORTACION
-----------

Modulos -> .py
Paquetes -> .pyd

Dos formas para importar
import externo (importamos TODOS los objetos)
from externo import estrategia (importamos los objetos QUE QUERAMOS)

Iguales en cuanto rendimiento
'''
import CodigoPractica.externo as externo # Tienen que estar en el mismo directorio
# Para usar los objetos importados, se usan como si estuvieran en el mismo programa

# Ejemplo de lectura de ficheros
def Main():
    mazo = externo.Mazo(1,2)
    print(mazo.reparte())
    
    # Tratamiento de excepciones a la hora de abrir un fichero
    try:
        # Apertura del fichero (modo lectura -> r)
        with open('/workspaces/BLACKJACK-PAR-1/Sesiones/ejemplo.txt','r') as fichero:
            # Leer contenido del fichero
            contenido = fichero.read()
            print (contenido)
        # El fichero se cierra de forma automatica una vez acaba la indentacion del with

    except IOError as e:
        # En esta parte del codigo, hubo un error y los mostramos por pantalla
        print (f"Error a la hora de abrir el fichero: {e}")
        
        
    try:
        with open('/workspaces/BLACKJACK-PAR-1/numeros.txt','w') as file:
            # Escribo el contenido en el archivo
            for i in range (0,201,2):
                file.write(f"{i}\n")
            
    except IOError as error:
        print("Error a la hora de abrir el archivo: {error}")
    

if __name__ == "__main__":
    Main()
    
    print(jugador)