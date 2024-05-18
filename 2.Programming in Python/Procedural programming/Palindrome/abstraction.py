from abc import ABC, abstractmethod


class Palindrome(ABC):
    @abstractmethod
    def isPalindrome(self, text: str) -> bool:
        """check if text is palindrome

        Args:
            text (str): text to check

        Returns:
            bool: true - if text is palindrome, else false
        """
        pass
