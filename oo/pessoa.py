class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    leticia = Pessoa(nome='Letícia')
    maria = Pessoa(leticia, nome='Maria')
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
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(maria.olhos)
    print(leticia.olhos)
    print(id(Pessoa.olhos), id(maria.olhos), id(leticia.olhos))
    print(Pessoa.metodo_estatico(), maria.metodo_estatico())
