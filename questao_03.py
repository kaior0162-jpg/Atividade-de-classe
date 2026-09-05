class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

Givanna = Pessoa("Geovanna", "26", "64", "1,69")
 
tiba = Pessoa("Tiba", "48", "72", "1,62")    

print(f"{Givanna.nome}")