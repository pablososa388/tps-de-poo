from continente import Continente

class Pais:
    def __init__(self, nombre,capital, superficie,continente):
        self.__nombre= nombre
        self.__capital=capital
        self.__superficie= superficie
        self.__continente= continente
        self.__listadeprovincias=[]
        self.__paiseslimitrofes=[]



    @property
    def nombre(self):
        return self.__nombre
        
    @property
    def capital(self):
        return self.__capital
    @property
    def superficie(self):
        return self.__superficie
    @property
    def continente(self):
        return self.__continente
    @property
    def listadeprovincias(self):
        return self.__listadeprovincias
    @property
    def paiseslimitrofes(self):
        return self.__paiseslimitrofes
    

        ##, agregarProvincia(Provincia p), agregarLimitrofe(Pais p).
    def agregarProvincia(self, nuevaprov):
        self.__listadeprovincias.append(nuevaprov)
    def agregarLimitrofe(self, limita):
        self.__paiseslimitrofes.append(limita)
    
    def __str__(self):
        provincias= ""
        for provincia in self.__listadeprovincias:
            provincias+=f"\n - {provincia.nombre}"
        
        paises=""
        for pais in self.__paiseslimitrofes:
            paises+=f"\n - {pais.nombre}"

        return f"Nombre del pais: {self.__nombre},\n Capital: {self.__capital},\n superficie: {self.__superficie}km^2 ,\n Continente al que pertenece: {self.__continente} ,\n Provincias: {provincias} ,\n Países limítrofes:{paises} "