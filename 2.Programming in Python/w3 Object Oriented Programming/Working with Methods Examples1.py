class A:
    def c(self):
        return "Function inside A"

class B:
    def c(self):
        return "Function inside B"

class C(A, B):
    def c(self): # type: ignore
        return "Function inside C"

class D(A, C): # type: ignore
    pass

d = D()
print(d.c()) # type: ignore