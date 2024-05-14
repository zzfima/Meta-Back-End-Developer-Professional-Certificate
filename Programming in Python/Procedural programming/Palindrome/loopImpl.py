from abstraction import Palindrome


class LoopPalindrome(Palindrome):
    """Loop implementation"""

    def isPalindrome(self, text: str) -> bool:
        right = len(text) - 1
        left = 0
        while right - left >= 1:
            if text[right] != text[left]:
                return False
            left += 1
            right -= 1
        return True
