class A:
    def d(self):
        return "Function inside A"


class B:
    def d(self):
        return "Function inside B"


class C:
    def d(self):
        return "Function inside C"


class D(A, B):
    def d(self):  # type: ignore
        return "Function inside D"


class E(B, C):
    def d(self):  # type: ignore
        return "Function inside E"


class F(E, D, C):  # type: ignore
    pass


f = F()
print(f.d())
print(F.mro())
