class A:
    a = "A"


class B:
    b = "B"


class C(A, B):
    pass


print("", end="\n")
c1 = C()
print(c1.a + " " + c1.b)
