
# # Inicio del flujo del codigo

# # Funcion para imprimir la matriz por pantalla
# def verMatriz (m):
#     for i in range(2):
#         for j in range(2):
#             print (m[i],[j], end=" ")
#         print ()
        
# def llenarMatriz (m):
#     for i in range(2):
#         for j in range(2):
#             m[i][j] = 4


# if __name__=="__main__":
    
#     # Mejor definir la matriz aqui
#     # Definimos una matriz, usamos for para manipular la matriz
#     matriz1=[[0,1],[2,3]]
    
#     NUM_FIL = 2
#     NUM_COL = 2
#     matriz2 = [[0 for col in range(NUM_COL)],[0 for fil in range (NUM_FIL)]]
    
#     print ("Metodo main()")
#     verMatriz (matriz1)
#     llenarMatriz (matriz2)
#     print (matriz2)



# objetos (para manos en blackjack) coches
# necesitamos una plantilla -> clase

# definicion de la clase coche
class Coche:
    # propiedades que quiero que tenga la clase en cuestion
    def __init__(self, marca, modelo, color):
        #defino los atributos del coche
        self.marca = marca
        self.modelo = modelo
        self.color = color
        
    # Ver informacion del coche
    def mostrarCoche(self):
        print (f"Marca:{self.marca}")
        print (f"Modelo:{self.modelo}")
        print (f"Color:{self.color}")
        
if __name__ == "__main__":
    # Crear coche: instanciar la clase coche
    coche = Coche("Toyota", "Corola", "Rojo")
    coche.mostrarCoche()