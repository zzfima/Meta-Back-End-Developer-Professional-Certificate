from abc import ABC


class Engine(ABC):
    def __init__(self):
        print("Engine ctor")
        self._a = 2  # protected
        self.__b = 3  # private


class Diesel(Engine):
    def __init__(self):
        print("Diesel ctor")
        super().__init__()
        self.k = 4

    def printState(self):
        print(self.k)
        print(self._a)
        # cannot access private: print(self.__b)


d = Diesel()
d.printState()
print(d.k)
print(d._a)
# cannot access private: print(d.__b)
