class Cancha:
    def __init__(self, numero, tipo_superficie):
        self.numero = numero
        self.tipo_superficie = tipo_superficie
        self.__turno = [ ]  ##lo ponemos como privado
        self.indice = indice
  ##GETTER:
        @property
    def turnos (self):
           return self.__turno

##MÉTODOS:
        def reservar(self, turno):
            self.__turnos.append(turno)
        print(f"Turno {turno} reservado en la cancha {self.numero}, tipo de superficie: {self.tipo_superfice}")
    
        def cancelar(self,turno):
            self.__turnos.remove(turno)
        print(f”El turno {turno} reservado en la cancha {self.cancha} de superficie {self.tipo_suuperficie} ha sido cancelado”)
    
        def modificar (self,indice,turno):
             if indice<len(self.__turnos):
             self.__turno[indice] = turno
         print(f"turno modificado exitosamente: {turno} en la cancha número {self.cancha} de superficie {self.superficie}")
             else print("el indice es inválido")

