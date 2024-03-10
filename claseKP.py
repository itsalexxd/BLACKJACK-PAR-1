class Madre():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def presentarse(self):
        print("Mi nombre es", self.nombre, "y tengo", self.edad, "años de edad")
        
mimadre = Madre("Bulma", "34")
mimadre.presentarse()



class Padre(Madre):
    pass
mipadre = Padre("vegeta", "37")
mipadre.presentarse()