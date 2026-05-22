from datetime import time
from cancha import Cancha

class Turnos:
    def __init__(self,nombre,hora):
        self.__horario= time(hora,0)
        self.__nombreyapellido= nombre



    @property
    def horario(self):
        return self.__horario
    @property
    def nombreyapellido(self):
        return self.__nombreyapellido
    

    def __str__(self):

        return f"Nombre y apellido: {self.__nombreyapellido}, horario: {self.__horario}"
