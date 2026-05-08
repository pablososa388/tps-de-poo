from continente import Continente
from pais import Pais
class Provincia:
    def __init__(self, nombre):
        self.__nombre= nombre


    @property
    def nombre(self):
        return self.__nombre
    
    def __str__(self):
        return f"Nombre de la provincia: {self.__nombre}"