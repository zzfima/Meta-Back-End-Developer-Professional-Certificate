from server import calc
from server import calc as CLC  # alias

c = calc()
print("\n3 + 4 = {}".format(c.add(3, 4)))
c = CLC()
print("\n3 + 4 = {}".format(c.add(3, 4)))
