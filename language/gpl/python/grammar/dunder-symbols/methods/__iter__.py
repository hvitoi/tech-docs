# %%
# The __iter__ method makes an object "iterable"
# (i.e. usable in a `for` loop, `list(...)`, `sum(...)`, etc.)


from collections.abc import Iterable  # Python 3.9+
# from typing import Iterable  # deprecated!


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add(self, song):
        self.songs.append(song)

    def __iter__(self):
        for song in self.songs:
            yield song


favs: Iterable = Playlist("Favourites")
favs.add("Bohemian Rhapsody")
favs.add("Imagine")
favs.add("Hey Jude")

for song in favs:
    print(song)
