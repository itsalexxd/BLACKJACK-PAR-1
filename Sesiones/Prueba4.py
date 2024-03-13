# HERENCIA DE CLASES

class Vehiculo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
    
    def mostrarInfo(self):
        print(f"Informacion: {self.marca},{self.modelo}")
        
        
class Automovil(Vehiculo):
    def __init__(self,marca,modelo,cilindrada):
        super().__init__(marca,modelo)
        self.cilindrada = cilindrada
        
    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"Cilindrada: {self.cilindrada}")
        
def Main():
    vehiculo = Vehiculo("BMW", "E46")
    vehiculo.mostrarInfo()
    
    coche = Automovil("Toyota", "Supra", "1200CV")
    coche.mostrarInfo()
    
if __name__ == "__main__":
    Main()