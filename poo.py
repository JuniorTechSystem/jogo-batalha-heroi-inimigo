""" 
POO - PROGRAMÇÃO ORIENTADA Á OBJETOS.

Classe exemplo
"""
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e minha idade é {self.idade} anos"

# Objetos é uma instância da classe.
pessoa1 = Pessoa("Junior", 31)
mensagem = pessoa1.saudacao()
print(mensagem)