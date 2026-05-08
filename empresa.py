from pt2empleado import Empleado

class Empresa:
    def __init__(self):
        self.__empleados= []

    @property
    def empleados(self):
        return self.__empleados
    
    


    def registrarempleado(self, new_empleado):
        for empleado in self.__empleados:
            if empleado.dni==new_empleado.dni:
                return "el dni ya existe, no es válido"
            
        self.__empleados.append(new_empleado)

    def maxsueldo(self):
        max_sueldo= self.__empleados[0]
        for sueldoempleado in self.__empleados:
            
            if sueldoempleado.sueldo > max_sueldo.sueldo:
                max_sueldo = sueldoempleado

        return max_sueldo
    
    def sueldoprom(self)->float:
        acum= 0
        result=0
        for sueldos in self.__empleados:
            acum= acum +sueldos.sueldo

        result= acum/len(self.__empleados)
        return f"el sueldo proemdio es {result}"

