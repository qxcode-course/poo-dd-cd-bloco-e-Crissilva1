
from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id:str, tipo:str, horaEntrada:int):
        self.__id:str=id
        self.__tipo:str=tipo
        self.__horaEntrada:int=horaEntrada

    def get_Entrada(self):
        return self.__horaEntrada
    
    def get_id(self):
        return self.__id
    
    def get_tipo(self):
        return self.__tipo
    
    def set_Entrada(self, horaEntrada:int)->None:
        self.__horaEntrada = horaEntrada

    @abstractmethod
    def cacularValor(self, horaSaida:int)->None:
        pass

    def __str__(self):
        return f"{self.__id}:{self.__tipo}:{self.__horaEntrada}"
    
class Bicicleta(Veiculo):
    def __init__(self,id:str, tipo:str, horaEntrada:int):
        super(). __init__(id, tipo, horaEntrada)
        self.__id:str=id
    
    def cacularValor(self, horaSaida: int) -> None:
        return 
    
class Moto(Veiculo):
    def __init__(self, id:str, tipo:str, horaEntrada:int):
        super().__init__(id, tipo, horaEntrada)
        self.__id:str=id

    def cacularValor(self, horaSaida: int) -> None:
        return 
    
class Carro(Veiculo):
    def __init__(self, id:str, tipo:str, horaEntrada:int):
        self.__id:str=id

    def cacularValor(self, horaSaida: int) -> None:
        return 
    
class Estacionamento:
    def __init__(self, horaAtual:int):
        self.__horaAtual:int=horaAtual
        self.__veiculos:list[Veiculo]=[] 

    def procurarVeiculo(self,id:str)-> int:
        for index, veiculo in enumerate(self.__veiculos):
            if veiculo.get_id() == id:
                return index
        return -1
    
    def Estacionar(self, veiculo:Veiculo)->None:
        index = self.procurarVeiculo("id")
        if index !=-1:
            return 
       
