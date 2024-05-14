from abstraction import Palindrome
from recursiveImpl import RecursivePalindrome


def printIsPalindrome(text: str, pol: Palindrome) -> None:
    print(text, " is Palindrome? ", pol.isPalindrome(text))


pol = RecursivePalindrome()
printIsPalindrome("carerac", pol)
printIsPalindrome("mannam", pol)
printIsPalindrome("melkooklem", pol)
printIsPalindrome("nashasan", pol)
