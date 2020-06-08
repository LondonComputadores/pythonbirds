class Pessoa:
    def __init__(self, *filhos, nome=None, idade=37):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    alex = Pessoa(nome='Alex')
    alexandre = Pessoa(alex, nome='Alexandre') # p = Pessoa('Alexandre')
    print(Pessoa.cumprimentar(alexandre))
    print(id(alexandre))
    print(alexandre.cumprimentar())
    print(alexandre.nome)
    alexandre.nome = 'Alex'
    print(alexandre.nome)
    print(alexandre.idade)
    for filho in alexandre.filhos:
        print(filho.nome)
    alexandre.sobrenome = 'Paes'
    del alexandre.filhos
    print(alexandre.__init__)
    print(alex.__init__)


