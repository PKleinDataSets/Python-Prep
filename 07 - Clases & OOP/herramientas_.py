import copy
class Herramientas :
    #def __init__(self) -> None:
     #   pass
     
    def __init__(self, lista_numeros):
        if type(lista_numeros) != list :
            self.lista = []
            raise ValueError('Se ha creado una lista vacía. Se esperaba una lista de núemeros enteros')
        else:    
            self.lista = lista_numeros 
    
    def __esPrimo(self, n) :
        if (type(n) != int or n <= 0):
            print("Debe ser un numero entero y positivo")
        else:
            if n == 1 :
                return False
            else:
                primo = True
                for i in range(2, int(n / 2)+1 ):
                    if n % i == 0:
                        primo = False
                        break 
                return primo
    
    def lista_primos(self):
        list_prim = []
        for i in self.lista :
            if self.__esPrimo(i):
                list_prim.append(i)
        return list_prim        
    
    def mas_repetido(self):
        list_ = copy.deepcopy(self.lista)
        cant = 0
        mas_repetido_ = 0
        veces = 0
        
        for i in range(len(list_)):
            cant = int(list_.count(list_[i]))
            if cant > veces:
                mas_repetido_ = list_[i]
                veces = cant           
        return mas_repetido_, veces    
    
    
    def mas_repetido_mayor(self, reverse_ = False):
        mas_repetido_ = 0
        veces = 0 
        rev_ = reverse_
        cant = 0
        list_ = copy.deepcopy(self.lista)
        
        if rev_ :
            list_.sort(reverse = True)
        else :
            list_.sort(reverse = False)    
    
        for i in range(len(list_)):
            cant = int(list_.count(list_[i]))
            if cant > veces:
                mas_repetido_ = list_[i]
                veces = cant
            
        return mas_repetido_, veces   
    
    def __conversion_grados(self, valor, origen, destino):
        val_ = ['celsius', 'farenheit', 'kelvin']
        if (origen != destino and ((origen in val_) and (destino in val_))):
            result = 0
            if (origen == 'celsius' and destino == 'farenheit'):
                result = (valor * 9 / 5) + 32
            elif(origen == 'celsius' and destino == 'kelvin'):
                result = valor + 273.15
            elif(origen == 'farenheit' and destino == 'kelvin'):
                result = ((valor - 32) / (9/5) ) + 273.15
            elif(origen == 'farenheit' and destino == 'celsius'):
                result = ((valor - 32) / (9/5) ) 
            elif(origen == 'kelvin' and destino == 'celsius'):
                result = valor - 273.15   
            elif(origen == 'kelvin' and destino == 'farenheit'):
                result = valor * (9/5) - (273.15 * (9/5)) + 32
            return round(result,2)
        else :
            print('''Valores invalidos : los valores validos son : {} y el  
                  valor de origen y el de destino deben ser distintos'''.format(val), )
    
    def conversion_grados(self, origen, destino):
        val_ = ['celsius', 'farenheit', 'kelvin']
        if (origen != destino and ((origen in val_) and (destino in val_))):
            for i in self.lista:
                print(i, 'grados', origen, 'son', 
                    self.__conversion_grados(i, origen, destino),'grados',destino) 
        else :
            print('''Valores invalidos : los valores validos son : {} y el  
                  valor de origen y el de destino deben ser distintos'''.format(val_), )        

    def __factorial(self, numero):
        if(type(numero) != int):
            return 'El numero debe ser un entero'
        if(numero < 0):
            return 'El numero debe ser pisitivo'
        result = 1
        if numero > 1 :
            for i in range(1, numero+1):
                result *= i
        return result  
    
    def factorial(self):
        fact = []
        for i in self.lista:
            if (type(i) == int and i >= 0):
                fact.append(self.__factorial(i))  
        return fact   