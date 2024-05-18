class Employee:
    def __init__(self, name: str, last: str) -> None:
        self.name = name
        self.last = last


class Supervisor(Employee):
    def __init__(self, name: str, last: str, password: str) -> None:
        super().__init__(name, last)
        self.password = password


class Chief(Employee):
    def leaveRequest(self, days: int):
        return "May i take a leave for a {} days?".format(days)


adrian = Employee("Adrian", "A")
emely = Chief("Emely", "E")
juno = Chief("Juno", "J")
print(emely.leaveRequest(5))