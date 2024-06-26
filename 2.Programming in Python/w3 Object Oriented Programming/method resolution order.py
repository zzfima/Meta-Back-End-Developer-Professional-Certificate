print(
    "method resolution order - determines the order in which a given method is searched"
)
"""

     ^
     |
     |
     |
     |
     ----------->

"""


# simple inheritance
class A:
    def f1(self):
        pass


class B(A):
    def f2(self):
        super().f1()


print("simple inheritance MRO: {}".format(B.mro()))


# multiple inheritance
class C:
    def f1(self):
        pass


class D:
    def f2(self):
        pass


class E(C, D):
    def f3(self):
        super().f1()
        super().f2()


print("multiple inheritance MRO: {}".format(E.mro()))


# multilevel inheritance
class F:
    def f1(self):
        pass


class G(F):
    def f2(self):
        super().f1()


class H(G):
    def f3(self):
        super().f2()
        super().f1()


print("multilevel inheritance MRO: {}".format(H.mro()))


# diamond inheritance
class I:
    def f1(self):
        pass


class J(I):
    def f2(self):
        super().f1()


class K(I):
    def f3(self):
        super().f1()


class L(J, K):
    def f4(self):
        super().f3()
        super().f2()
        super().f1()


print("diamond inheritance MRO: {}".format(L.mro()))
help(L)