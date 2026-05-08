class Empleado:
    __SALARIO_MINIMO_VITAL= 300000
    def __init__(self,nombre, dni,sueldo):
        self.dni= dni
        self.sueldo= sueldo
        self.__nombre= nombre
    ##setters y getters para los atributos priv
    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self,dni):
        self.__dni=dni
      
        

    @property
    def sueldo(self):
        return self.__sueldo
    
    @sueldo.setter
    def sueldo(self,sueldo):
        if sueldo< self.__SALARIO_MINIMO_VITAL:
            self.__sueldo= self.__SALARIO_MINIMO_VITAL
        else:
             self.__sueldo= sueldo

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre


    ##métodos:

