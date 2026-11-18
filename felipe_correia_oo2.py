#  # Exercício 1  
# class Endereco:
#     def __init__(self,rua,numero,cidade):
#         self.rua=rua
#         self.cidade = cidade
#         self.numero =numero



# class Pessoa:
#     def __init__(self,nome,rua,cidade,numero):
#         self.nome = nome
#         self.endereco = Endereco(rua,cidade,numero)
    
#     def apresentar(self):
#         return print(f"{self.nome} mora na Rua {self.endereco.rua}, {self.endereco.numero} - {self.endereco.cidade}")


# nome = str(input("Qual o seu nome? \n> "))
# rua = str(input("Qual o nome da rua aonde você mora? \n> "))
# numero = str(input("Qual o número da sua residência? \n> "))
# cidade = str(input("Qual a cidade você mora? \n> ")) 


# P1 = Pessoa(nome,rua,numero,cidade)

# P1.apresentar();



 # Exercício 2

# class Livro:
#     def __init__(self,nome,autor,ano_pub):
#         self.nome = nome
#         self.autor = autor
#         self.ano_pub = ano_pub

#     def __str__(self):
#         return f"{self.nome} ({self.autor}, {self.ano_pub})"

#     def __eq__(self,outro):
#         comparacao = self.nome == outro.nome and self.autor == outro.autor
#         return comparacao



# # nome = str(input("Nome do livro \n> "))
# # autor = str(input("Autor do livro \n> "))
# # ano_publicacao = str(input("Ano de publicação do livro \n> "))


# # L1= Livro(nome,autor,ano_publicacao)
# L1= Livro("Farenheit 451","Ray BradBury","1985")

# L2 = Livro("Dom Casmurro","Machado de Assis","1899")

# print(f"Exemplares: \n{L1}\n{L2}")
# print(f"É o mesmo livro? {L1 == L2}")

 # Exercício 3

class Biblioteca:
    def __init__(self):
        self.livros = []  # A biblioteca guarda vários livros em uma lista

    def adicionar(self, livro):
        # O 'not in' usa o __eq__ do Livro para verificar se já existe
        if livro not in self.livros:
            self.livros.append(livro)

    def listar(self):
        for l in self.livros:
            print(l)  # O print chama automaticamente o __str__ do Livro

    def buscar_por_autor(self, autor):
        livros_do_autor = []
        for l in self.livros:
            if l.autor == autor:
                livros_do_autor.append(l)
        return livros_do_autor


# --- Teste (igual ao slide) ---
b = Biblioteca()
L1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
L2 = Livro("Quincas Borba", "Machado de Assis", 1891)

b.adicionar(L1)
b.adicionar(L2)
b.adicionar(L1)  # repetido: não entra por causa da verificação e do __eq__

b.listar()
print(len(b.buscar_por_autor("Machado de Assis")))