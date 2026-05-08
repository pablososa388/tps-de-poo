class Continente:
    def __init__(self,nombre):
        self.__nombre= nombre
        self.__lista_de_paises= []


    @property 
    def paises(self):
        return self.__lista_de_paises
        
    @property
    def nombre(self):
        return self.__nombre
    
    def agregarPais(self, nuevopais):
        self.__lista_de_paises.append(nuevopais)


    def __str__(self):
        paises=""
        for pais in self.__lista_de_paises:
            paises+= f"\n - {pais.nombre}"
        return f"Nombre del continente: {self.__nombre} ,\n Paises del continente: {paises}"
