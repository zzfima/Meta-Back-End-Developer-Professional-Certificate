class A:
   def __init__(self, c: int):
       print("---------Inside class A----------") #4
       self.c = c
   print("\nPrint inside A.") #1

   def alpha(self):
       c = self.c + 1
       return c

print(dir(A)) #2
print("Instantiating A..") #3
a = A(1)
print(a.alpha()) #5

class B:
   def __init__(self, a: A):
       print("---------Inside class B----------") #10
       self.a = a

   print(a.alpha()) #6
   d = 5
   print(d) #7
   print(a) #8

print("Instantiating B..") #9
b = B(a)
print(a) #11