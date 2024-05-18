class Recipe:
    def __init__(self, dish: str, items: list[str], time: int) -> None:
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        print(
            "the {} has {} and takes {} minutes to prepare".format(
                self.dish, str(self.items), str(self.time)
            )
        )

print('')
pizza = Recipe("margaritta", ["cheese", "bread"], 45)
pizza.contents()
print(pizza.dish)