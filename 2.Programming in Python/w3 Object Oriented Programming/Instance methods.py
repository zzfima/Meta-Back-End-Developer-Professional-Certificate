class Payslips:
    def __init__(self, name: str, payment: str, amount: float) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = "yes"

    def status(self) -> str:
        if self.payment == "yes":
            return "{} is paid {}".format(self.name, self.amount)
        else:
            return "{} did not paid yet".format(self.name)


nathan = Payslips("Nathan", "no", 1000)
print(nathan.status())
