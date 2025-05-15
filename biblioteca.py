class Atleta():
    def __init__(self, peso):
        self.aposentado = False
        self.aquecido = False
        self.peso = peso
    def aposentar(self):
        if self.aposentado == False:
            self.aposentado = True
            print("O atleta agora está aposentado!")
        else:
            print("O atleta já está aposentado!")
    def aquecer(self):
        if self.aposentado == True:
            print("O atleta não pode aquecer pois está aposentado")
        elif self.aquecido == True:
            print("O atleta já está aquecido")
        else:
            print("O atleta está aquecendo...")
            self.aquecido = True
            
class Corredor(Atleta):
    def __init__(self, peso):
        super().__init__(peso)
        self.correndo = False
    def correr(self):
        if self.aquecido == False:
            print("O atleta não está aquecido, ele não pode correr")
        elif self.aposentado == True:
            print("O atleta está aposentado e não pode correr")
        elif self.correndo == True:
            print("O atleta já está correndo!")
        else:
            self.correndo = True
            print("O atleta começou a correr!!")
                  
class Nadador(Atleta):
    def __init__(self, peso):
        super().__init__(peso)
        self.nadando = False
    def nadar(self):
        if self.aquecido == False:
            print("O atleta não está aquecido, ele nao pode nadar!")
        elif self.aposentado == True:
            print("O atleta está aposentado e não pode nadar")
        elif self.nadando == True:
            print("O atleta já está nadando!")
        else:
            self.nadando = True
            print("O atleta foi nadar...")
            
class Ciclista(Atleta):
    def __init__(self, peso):
        super().__init__(peso)
        self.pedalando = False
    def pedalar(self):
        if self.aquecido == False:
            print("O atleta não está aquecido, ele nao pode nadar!")
        elif self.aposentado == True:
            print("O atleta está aposentado e não pode pedalar")
        elif self.pedalando == True:
            print("O atleta já está pedalando!")
        else:
            self.pedalando = True
            print("O atleta foi pedalar...")

class TriAtleta(Corredor, Nadador, Ciclista):
    def __init__(self, peso):
        super().__init__(peso)
    #Usando o polimorfismo:
    def correr(self):
        if self.pedalando == True:
            print("O atleta está pedalando e não pode correr!")
        elif self.nadando == True:
            print("O atleta está nadando e não pode correr!")
        else:
            super().correr()#pega todas as instruções do metodo correr da classe Corredor
    def pedalar(self):
        if self.correndo == True:
            print("O atleta está correndo e não pode pedalar!")
        elif self.nadando == True:
            print("O atleta está nadando e não pode pedalando!")
        else:
            super().pedalar()
    def nadar(self):
        if self.pedalando == True:
            print("O atleta está pedalando e não pode nadar!")
        elif self.correndo == True:
            print("O atleta está correndo e não pode nadar!")    
        else:
            super().nadar()