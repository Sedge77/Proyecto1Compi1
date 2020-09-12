class Token():

    def __init__(self,Tipo,caracter): #Constructor de la clase animal
        self.Tipo=Tipo  #usamos la notacion __ por que lo estamos encapsulando, ninguna subclase puede acceder a el, es un atributo privado
        self.caracter=caracter
        

    def setTipo(self,Tipo):
        self.__Tipo=Tipo   
          

    def getTipo(self):
        return self.__Tipo   

    def setcaracter(self,caracter):
        self.__caracter=caracter   
          

    def getcaracter(self):
        return self.caracter   

    def miestado(self):
            
            print("Tipo: ",self.__Tipo,"--------->"+"Token: ",self.__caracter) 
                