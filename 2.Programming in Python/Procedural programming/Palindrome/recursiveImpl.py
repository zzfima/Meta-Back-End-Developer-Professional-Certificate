from abstraction import Palindrome


class RecursivePalindrome(Palindrome):
    """Recursive implementation of Palindrome"""

    # override abstract method
    def isPalindrome(self, text: str) -> bool:
        textLen = len(text)
        if textLen <= 1:
            return True
        if text[0] != text[textLen - 1]:
            return False
        return self.isPalindrome(text[1 : textLen - 1])
