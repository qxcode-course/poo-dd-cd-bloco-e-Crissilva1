
from abc import ABC

class Animal(ABC): #abs
    def __init__(self, nome:str):
        self.nome:str=nome 

    def apresentar_nome(self):
        print (f"eu sou um(a) {self.nome}!") 

    def fazer_som(self):
        pass
    def mover(self):
        pass   


class leao(Animal):
    def __init__(self, nome:str):
        super().__init__(nome)

    def fazer_som(self):
        print("rosnar")

    def mover(self):
        print("caminhando na floresta")



class Elefante(Animal):
    def __init__(self, nome:str):
        super().__init__(nome)

    def fazer_som(self):
        print("bramido")

    def mover(self):
        print("caminhando no zoologico")

class Cobra(Animal):
    def __init__(self, nome:str):
        super().__init__(nome)
    
    def fazer_som(self):
        print("sshhh")

    def mover(self):
        print("rastejando na mata")

def apresentar(animal:Animal):
    animal.apresentar_nome()
    animal.fazer_som()
    animal.mover()
    print("Tipo:", type (animal).__name__)
    print()

def main():
    animais:list[Animal]=[
        leao("simba"),
        Elefante("dumbo"),
        Cobra("cascavel")
    ]
    for a in animais:
       apresentar(a)

main()