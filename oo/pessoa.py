class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

class Homem(Pessoa):
    pass

class Mutante(Homem):
    olhos = 3

if __name__ == '__main__':
    leticia = Homem(nome='Letícia')
    maria = Homem(leticia, nome='Maria')
    print(Pessoa.cumprimentar(maria))
    print(id(maria))
    print(maria.cumprimentar())
    print(maria.nome)
    print(maria.idade)
    for filho in maria.filhos:
        print(filho.nome)
    maria.sobrenome = 'Alves'
    del maria.filhos
    maria.olhos = 1
    del maria.olhos
    print(maria.__dict__)
    print(leticia.__dict__)
    print(Pessoa.olhos)
    print(maria.olhos)
    print(leticia.olhos)
    print(id(Pessoa.olhos), id(maria.olhos), id(leticia.olhos))
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    rint(isinstance(leticia, Pessoa))
    rint(isinstance(leticia, Homem))
    print(leticia.olhos)

