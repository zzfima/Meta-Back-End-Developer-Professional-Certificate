def sum_of_a_and_b(a, b):
    return a + b


# argument args is tuple
def sum_of_many(*args):
    s = 0
    for v in args:
        s += v
    return s


# argument kwargs is dictionary - keyword args
def sum_of_many_ex(**kwargs):
    s = 0
    products = ""
    for k, v in kwargs.items():
        s += v
        products += k
        products += " "
    return products, s


print(sum_of_a_and_b(2, 3))
print(sum_of_many(2, 3, 4, 5))
r = sum_of_many_ex(coffee=2, milk=3, cake=14)
print(r[0], " costs ", r[1])
