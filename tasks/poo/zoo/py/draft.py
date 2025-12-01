
import abc

class Animal(abc.ABC): #abs
    def __init__(self, nome:str):
        self.nome:str=nome 

    def apresentar_nome(self, nome:str):
        print (f"eu sou um {nome}!")    


class leao(Animal):
    def __init__(self, nome:str):
        super().__init__(nome)

class Elefante(Animal):
    def __init__(self, nome:str):
        super().__init__(nome)

    def fazer_som(self):
        print("roar")

    def mover(self):
        print("caminhada furtiva")        