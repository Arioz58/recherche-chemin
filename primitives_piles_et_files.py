class Pile:
    def __init__(self):
        self.__liste__ = [] # attribut liste privé

    def est_vide(self) -> bool:
        return len(self.__liste__) == 0

    def depiler(self):
        return self.__liste__.pop()

    def empiler(self, truc) -> None:
        self.__liste__.append(truc)

class File:
    def __init__(self):
        self.__liste__ = [] # attribut liste privé

    def est_vide(self) -> bool:
        return len(self.__liste__) == 0

    def defiler(self):
        return self.__liste__.pop(0)

    def enfiler(self, truc) -> None:
        self.__liste__.append(truc)
