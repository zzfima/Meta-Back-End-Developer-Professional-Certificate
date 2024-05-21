"""
method resolution order - determines the order in which a given method is searched

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
