'''criar uma classe'''

class Carro:

    def __init__(self, cor, marca, linha, combustivel):
        self.cor = cor
        self.marca = marca
        self.linha = linha
        self.combustivel = combustivel

'''Criando um objeto'''

polo = Carro("branco", "volkswagem", "Polo", "gasolina")

Mustang = Carro("verde", "ford", "Mustang", "gasolina")

Prius = Carro("vermelho", "toyota", "Prius", "eletrico")

Golf = Carro("azul", "volkswagem", "Golf", "diesel")

'''Mostrando na tela'''

print(f"A cor do {Prius.linha} é {Prius.cor}")