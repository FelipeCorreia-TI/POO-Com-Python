 # Exercício 1  
class Endereco:
    def __init__(self,rua,numero,cidade):
        self.rua=rua
        self.cidade = cidade
        self.numero =numero



class Pessoa:
    def __init__(self,nome,rua,cidade,numero):
        self.nome = nome
        self.endereco = Endereco(rua,cidade,numero)
    
    def apresentar(self):
        return print(f"{self.nome} mora na Rua {self.endereco.rua}, {self.endereco.numero} - {self.endereco.cidade}")


nome = str(input("Qual o seu nome? \n> "))
rua = str(input("Qual o nome da rua aonde você mora? \n> "))
numero = str(input("Qual o número da sua residência? \n> "))
cidade = str(input("Qual a cidade você mora? \n> ")) 


P1 = Pessoa(nome,rua,numero,cidade)

P1.apresentar();


    










 # Exercício 2





 # Exercício 3