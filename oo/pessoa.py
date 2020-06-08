class Pessoa:
    olhos = 2

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
    alexandre.olhos = 1 #ver agora que essa id é diferente, de 1 para 2
    del alexandre.olhos # agora o id passou de 2 para 3
    print(alexandre.__init__)
    print(alex.__init__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(alexandre.olhos)
    print(alex.olhos)
    print(id(Pessoa.olhos), id(alexandre.olhos), id(alex.olhos))


