class Entero:
    def __init__(self, numero):
        self.__numero = numero

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    # Calcula el cuadrado de n
    def cuadrado(self):
        return self.__numero ** 2
    
    def esPar(self)->bool:
        if self.__numero %2==0:
            return True
        else : 
            return False
    
    def esImpar(self)->bool:
        if self.__numero %2 !=0:
            return False
        else: 
            return True
    

    def factorial(self):
        fact=1
        result= self.__numero
        while fact>0:
            result= result * fact
            fact= fact - 1


    def esPrimo(self):
       
        for numeros in range(2,self.__numero):

            if self.__numero%numeros ==0:
                return False   
        return True
    


        
        
         
              











    ##Agregue los siguientes métodos a la clase respetando el encapsulamiento: esPar(), esImpar(), factorial(), esPrimo().