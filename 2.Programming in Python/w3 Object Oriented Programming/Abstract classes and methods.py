from abc import ABC, abstractmethod
from typing import override


class EmployeeBase(ABC):
    @abstractmethod
    def printName(self):
        pass


class Boss(EmployeeBase):
    @override
    def printName(self):
        print("I am a boss")

class Cleaner(EmployeeBase):
    @override
    def printName(self):
        print("I am a cleaner")
        
        
def employeePrinter(e: EmployeeBase):
    e.printName()
    
print('')    
e1 = Boss()
employeePrinter(e1)
e2 = Cleaner()
employeePrinter(e2)