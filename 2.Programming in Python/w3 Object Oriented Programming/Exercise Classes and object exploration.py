class A:
    def __init__(self, c: int):
        print("---------Inside class A----------")
        self.c = c

    print("Print inside A.")

    def alpha(self):
        c = self.c + 1
        return c


print(dir(A))
print("Instantiating A..")
# a = A(1)
# print(a.alpha())


class B:
    def __init__(self, a: int):
        print("---------Inside class B----------")
        self.a = a

    # print(a.alpha())
    d = 5
    print(d)
    # print(a)


print("Instantiating B..")
# b = B(a)
# print(a)
