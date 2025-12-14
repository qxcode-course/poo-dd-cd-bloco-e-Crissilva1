
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
    
    def set_Entrada(self, horaEntrada:int):
        self.__horaEntrada = horaEntrada

    @abstractmethod
    def calcularValor(self, horaSaida:int)->float:
        pass

    def __str__(self):
        return f"{self.__id}:{self.__tipo}:{self.__horaEntrada}"
    
class Bike(Veiculo):
    def __init__(self,id:str, horaEntrada:int=0):
        super(). __init__(id, "Bike" ,horaEntrada)
        

    def calcularValor(self, horaSaida: int)->float:
        return 3.0
    
class Moto(Veiculo):
    def __init__(self, id:str, horaEntrada:int=0):
        super().__init__(id, "Moto", horaEntrada)
        

    def calcularValor(self, horaSaida: int)->float:
        tempo= horaSaida - self.get_Entrada()
        valor= tempo / 20
        return valor
    
class Carro(Veiculo):
    def __init__(self, id:str, horaEntrada:int=0):
        super().__init__(id, "Carro", horaEntrada)
        
    def calcularValor(self, horaSaida: int)->float :
        tempo= horaSaida - self.get_Entrada()
        valor= max(tempo/10, 5.0)
        return valor

        
    
class Estacionamento:
    def __init__(self, horaAtual:int):
        self.__horaAtual:int=horaAtual
        self.__veiculos:list[Veiculo]=[] 

    def get_horaAtual(self):
        return self.__horaAtual

    def procurarVeiculo(self,id:str)-> int:
        for index, veiculo in enumerate(self.__veiculos):
            if veiculo.get_id() == id:
                return index
        return -1
    
    def Estacionar(self, veiculo:Veiculo)->None:
        if self.procurarVeiculo(veiculo.get_id()) !=-1:
            return
        veiculo.set_Entrada(self.__horaAtual)
        self.__veiculos.append(veiculo)
    
    def pagar(self, id:str):
        index=self.procurarVeiculo(id)
        if index == -1:
            return None
        veiculo=self.__veiculos[index]
        chegada=veiculo.get_Entrada()
        saida= self.__horaAtual
        valor= veiculo.calcularValor(saida)

        tipo=veiculo.get_tipo()

        self.__veiculos.pop(index)
        return f"{tipo} chegou {chegada} saiu {saida}. Pagar R$ {valor:.2f}"
    
    def sair(self, id:str)->str|None:
        index=self.procurarVeiculo(id)
        if index == -1:
            return None
        
        veiculo = self.__veiculos[index]

        saida=self.__horaAtual
        valor=veiculo.calcularValor(saida)
        tipo=veiculo.get_tipo()

        self.__veiculos.pop(index)
        return f"{tipo} saiu {saida}. Pagar R$ {valor:.2f}"
        



    def passarTempo(self, tempo:int)->None:
        self.__horaAtual += tempo

    def __str__(self)->str:
        saida=""
        for veiculo in self.__veiculos:
            tipo=veiculo.get_tipo()
            id=veiculo.get_id()
            hora=veiculo.get_Entrada()
            prefix_id="_____"
            prefix_tipo="_____"

        
            if tipo=="Bike":
                prefix_id = "_____"
                prefix_tipo = "______"  
            elif tipo=="Moto":
                prefix_id = "___"
                prefix_tipo = "______"  
            elif tipo == "Carro":
                prefix_id = "___"
                prefix_tipo = "_____"   

            saida += f"{prefix_tipo}{tipo} : {prefix_id}{id} : {hora}\n"

    
        saida += f"Hora atual: {self.__horaAtual}"
        return saida


        
        
def main():
    estacionamento=Estacionamento(0)
    while True:
        line:str=input()
        print("$"+ line)
        args:list[str]=line.split(" ")
        if args[0]=="end":
            break
        elif args[0]=="show":
            print(estacionamento)
        elif args[0]=="estacionar":
            tipo=args[1].lower()
            id=args[2]
            if tipo == "bike":
                estacionamento.Estacionar(Bike(id))
            if tipo == "moto":
                estacionamento.Estacionar(Moto(id))
            if tipo == "carro":
                estacionamento.Estacionar(Carro(id))
        elif args[0]=="tempo":
            estacionamento.passarTempo(int(args[1]))
        elif args[0]=="pagar":
           msg=estacionamento.pagar(args[1])
           if msg is not None:
               print(msg)
        elif args[0]=="sair":
            msg = estacionamento.sair(args[1])
            if msg is not None:
                print(msg)
        else :
            print ("comando invalido")
main()
        


        
    

       
