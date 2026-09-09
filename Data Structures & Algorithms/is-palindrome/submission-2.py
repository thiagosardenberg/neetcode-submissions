class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(char for char in s if char.isalpha() or char.isalnum())
        string = string.lower()
        print(string)
        if string[::-1] == string:
            return True
        return False