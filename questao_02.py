class Livro:

    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

livro1 = Livro("Dom Casmurro", "Machado de Assis", "1899")
 

print(f" O Titulo do livro é {livro1.titulo}")