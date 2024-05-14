def isPalindrome(text: str) -> bool:
    textLen = len(text)
    if textLen <= 1:
        return True
    if text[0] != text[textLen - 1]:
        return False
    return isPalindrome(text[1 : textLen - 1])


def printIsPalindrome(text: str) -> None:
    print(text, " is Palindrome? ", isPalindrome(text))


printIsPalindrome("carerac")
printIsPalindrome("mannam")
printIsPalindrome("melkooklem")
printIsPalindrome("nashasan")
