from abc import ABC


class Engine(ABC):
    # define members
    a = 99

    def __init__(self):
        print("Engine ctor")
        self._a = 2  # protected
        a = "granola"  # local variable, no self keyword
        self.__b = 3  # private
        print("local a: ", a)
        print("class a: ", self._a)


class Diesel(Engine):
    def __init__(self):
        print("Diesel ctor")
        super().__init__()
        self.k = 4

    def printState(self):
        print(self.k)
        print(self._a)
        # print(self.__b)


d = Diesel()
d.printState()
print(d.k)
print(Engine.a)
print(d.a)
# print(d._a)
# print(d.__b)
