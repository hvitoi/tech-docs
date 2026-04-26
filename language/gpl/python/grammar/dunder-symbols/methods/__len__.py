# %%
# __len__ makes len(obj) work.
# Implements collections.abc.Sized.


from collections.abc import Sized


class Bookshelf:
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def __len__(self):
        return len(self.books)


shelf: Sized = Bookshelf()
shelf.add("The Hobbit")
shelf.add("Dune")
shelf.add("1984")

len(shelf)  # 3
