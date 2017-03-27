#!/usr/bin/env python
#
# Python Exercises
# Shows the operation of a collections.namedtuple.
# Use in classes that there are no methods. It works in place of:
#
# class Message(object):
#    headers = []
#    content = None
#    from_addr = None
#    to_addr = None
#
# Or then:
#
# class Message(object):
#    def __init__(self, content, from_addr, to_addr):
#        self.headers = []
#        self.content = content
#        self.from_addr = from_addr
#        self.to_addr = to_addr
#
#    def add_header(self, info):
#        self.headers.append(info)
#
# Use:
#
# >>> import collections
# >>> Message = collections.namedtuple('Message', 'headers content from_addr to_addr')
# >>> m = Message([], "Hello, server!", "me", "some.address.com")
# >>> print m.content
# Hello, server!
# >>> m.headers.append("alguma informação")
# >>> print m.headers
# ["alguma informação"]
# >>> m.to_addr = "localhost"
# >>> print m.to_addr
# localhost
#
# >>> Dados = collections.namedtuple('Cadastro', 'nome, sobrenome, endereco, fones')
# >>> eu = Dados(nome='Vinicius',
#...            sobrenome='Assef',
#...            endereco='Rua 7 de setembro, 123',
#...            fones=['3322-1100', '9988-7766'])
#...


import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == "__main__":
    deck = FrenchDeck()
    print(len(deck))

