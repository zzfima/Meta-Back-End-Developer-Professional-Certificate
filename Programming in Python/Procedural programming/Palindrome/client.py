from abstraction import Palindrome
from recursiveImpl import RecursivePalindrome
from loopImpl import LoopPalindrome


def printIsPalindrome(text: str, pol: Palindrome) -> None:
    print(text, " is Palindrome? ", pol.isPalindrome(text))


print("*************")
pol = RecursivePalindrome()
printIsPalindrome("carerac", pol)
printIsPalindrome("mannam", pol)
printIsPalindrome("melkooklem", pol)
printIsPalindrome("nashasan", pol)

print("*************")
pol = LoopPalindrome()
printIsPalindrome("carerac", pol)
printIsPalindrome("mannam", pol)
printIsPalindrome("melkooklem", pol)
printIsPalindrome("nashasan", pol)
