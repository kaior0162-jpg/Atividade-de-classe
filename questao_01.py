class Bola:

    def __init__(self, cor, circunferencia, material, esporte):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
        self.esporte = esporte

futebol = Bola("verde", "30cm", "plastico", "futebol")

volei = Bola("azul", "50cm", "borracha", "volei")    

print(f"A bola 1 é de {futebol.esporte}")