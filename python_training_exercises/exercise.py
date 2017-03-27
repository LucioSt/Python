#!/usr/bin/env python
#
# This python file contains class exercises
#
#

class SerVivo(object):
    def idade(self):
        return self.idade

    def sexo(self):
        return self.sexo

    def EmiteSom(self): abstract

    def locomove(self): abstract


class Humano(SerVivo):
    def __init__(self, _idade_, _sexo_):
        self.nome  = "Humano"
        self.idade = _idade_
        self.sexo  = _sexo_

    def EmiteSom(self):
        return("Eu falo")

    def locomove(self):
        return("Andando com 2 pés")

class Cachorro(SerVivo):
    def __init__(self, _idade_, _sexo_):
        self.nome  = "Cachorro"
        self.idade = _idade_
        self.sexo  = _sexo_

    def EmiteSom(self):
        return("Eu Lato")

    def locomove(self):
        return("Andando com 4 patas")


class mamifero(object):
    @staticmethod
    def novoMamifero(MamiferoAdapter):
        _mamifero_ = MamiferoAdapter
        return _mamifero_



if __name__ == '__main__':
    ser = mamifero.novoMamifero(Humano(20,"Mulher"))




