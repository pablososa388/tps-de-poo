# class Motor:
#     def __init__(self, cilindrada, combustible):
#         self.cilindrada = cilindrada
#         self.combustible = combustible

#     def encender(self):
#         return f"Motor de {self.cilindrada}cc encendido ({self.combustible})"

#     def apagar(self):
#         return "Motor apagado"


# class Auto(Motor):
#     def __init__(self, marca, modelo, cilindrada, combustible):
#         super().__init__(cilindrada, combustible)
#         self.marca = marca
#         self.modelo = modelo

#     def describir(self):
#         return f"{self.marca} {self.modelo} - {self.encender()}"


# # Ejemplo de uso
# auto = Auto("Toyota", "Corolla", 1800, "nafta")
# print(auto.describir())
# print(auto.apagar())

# class Archivo:
#     def __init__(self, nombre, pesoEnMB):
#         print("Creando Archivo genérico...")
#         self.nombre = nombre
#         self.pesoEnMB = pesoEnMB


# class ArchivoVideo(Archivo):
#     def __init__(self, nombre, pesoEnMB, duracion):
#         super().__init__(nombre, pesoEnMB)
#         print("Creando Archivo de Video...")
#         self.duracion = duracion


# video = ArchivoVideo("pelicula.mp4", 700, 120)
# print(f"Nombre: {video.nombre}, Peso: {video.pesoEnMB}MB, Duración: {video.duracion}min")



class Animal:
    def hacerRuido(self):
        print("...")

class Gato(Animal):
    def hacerRuido(self): 
        print("Miau")

class Perro(Animal):
    def hacerRuido(self):  
        print("Guau")

class Vaca(Animal):
    def hacerRuido(self):
        print("Muuu")

p=Perro()
g=Gato()
v=Vaca()
l=[p,g,v]

for animales in l:
    animales.hacerRuido()



# class Persona:
#     def __init__(self, nombre, dni):
#         print("Creando Persona...")
#         self.nombre = nombre
#         self.dni = dni


# class Alumno(Persona):
#     def __init__(self, nombre, dni, legajo):
#         print("Creando Alumno...")
#         super().__init__(nombre, dni)
#         self.legajo = legajo


# class Docente(Persona):
#     def __init__(self, nombre, dni, cargo):
#         print("Creando Docente...")
#         super().__init__(nombre, dni)
#         self.cargo = cargo


# # Alumno avanzado contratado como docente auxiliar -> herencia múltiple
# class AlumnoDocente(Alumno, Docente):
#     def __init__(self, nombre, dni, legajo, cargo):
#         print("Creando AlumnoDocente...")
#         Alumno.__init__(self, nombre, dni, legajo)
#         Docente.__init__(self, nombre, dni, cargo)


# # Cuando se recibe, deja de ser Alumno y pasa a ser solo Docente
# # Con herencia clásica, esto NO se puede modelar: la clase de un objeto
# # no puede cambiar en tiempo de ejecución. Habría que crear un nuevo
# # objeto Docente y "descartar" el AlumnoDocente, perdiendo la identidad original.

# ad = AlumnoDocente("Juan", "12345678", "A-001", "Auxiliar")
# print(ad.nombre, ad.legajo, ad.cargo)