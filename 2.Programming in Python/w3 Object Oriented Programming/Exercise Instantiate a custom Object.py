class MyFirstClass:
    def __init__(self) -> None:
        print("Who wrote this?")
        self.index = "Author-Book"

    def hand_list(self, philosopher: str, book: str):
        print(self.index)
        print("{} wrote this book: {}".format(philosopher, book))


c = MyFirstClass()
c.hand_list("Plato", "Republic")
