def reverse(txt: str) -> str:
    return txt[::-1]


coffes = ["Espresso", "Latte", "Cappucino"]
reversed_coffees = map(reverse, coffes)
for c in reversed_coffees:
    print(c)
