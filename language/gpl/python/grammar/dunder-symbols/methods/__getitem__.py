# %%
# __getitem__ implements obj[key].
#
# Combined with __len__, the object becomes a Sequence.
# It also enables iteration as a fallback when __iter__ is missing
# (Python calls obj[0], obj[1], ... until IndexError).


from collections.abc import Sequence


class Bookshelf:
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def __getitem__(self, i):
        return self.books[i]

    def __len__(self):
        return len(self.books)


shelf = Bookshelf()
shelf.add("The Hobbit")
shelf.add("Dune")
shelf.add("1984")

shelf[0]    # 'The Hobbit'
shelf[-1]   # '1984'
shelf[0:2]  # ['The Hobbit', 'Dune']  (slicing works for free via list)
len(shelf)  # 3

for book in shelf:    # iteration via __getitem__ fallback
    print(book)

isinstance(shelf, Sequence)  # False — ABC requires registration or inheritance
