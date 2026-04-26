# %%
# An Iterator implements __iter__ AND __next__.
# - __next__: returns the next item, or raises StopIteration when done
# - __iter__: returns self (an iterator IS its own iterator)
#
# Iterators are one-shot: once exhausted, they cannot be restarted.


from collections.abc import Iterator  # Python 3.9+
# from typing import Iterator  # deprecated!


class CardDeck:
    def __init__(self):
        self.cards = ["A♠", "K♠", "Q♠", "J♠"]

    def __iter__(self):
        return self  # iterator returns itself

    def __next__(self):
        if not self.cards:
            raise StopIteration
        return self.cards.pop(0)  # draw the top card


deck: Iterator = CardDeck()

next(deck)  # 'A♠'
next(deck)  # 'K♠'

# `for` keeps drawing until the deck is empty:
for card in deck:
    print(card)

# Q♠
# J♠
