from datetime import time

class Cancha:

    def __init__(self,numero,superficie):
        self.__listadeturnos=[]
        self.__numero=numero
        self.__superficie=superficie



    @property
    def turnos(self):
        return self.__listadeturnos
    @property
    def numero(self):
        return self.__numero

    def reservarturno(self,nuevoturno):
        if nuevoturno.horario<time(14,0) and turnos.horario>time(23,0):
            return False
        for turnos in self.__listadeturnos:
            if nuevoturno.horario ==turnos.horario:
                return False                    
        self.__listadeturnos.append(nuevoturno)
        return True
    
    def cancelarturno(self, horario):

        for turno in self.__listadeturnos:
            if turno.horario==horario:
                self.__listadeturnos.remove(turno)
                return True
        return False
    

    def __str__(self):      
        texto = f"Cancha nro {self.__numero} - Superficie: {self.__superficie}\n"
        texto += "Turnos ocupados:\n"
        for turno in self.__listadeturnos:
            texto += f"  - {turno}\n"
        texto += "Turnos libres:\n"
        ocupados = [turno.horario.hour for turno in self.__listadeturnos]
        for hora in range(14, 24):
            if hora not in ocupados:
                texto += f"  - {hora}:00\n"
        return texto
