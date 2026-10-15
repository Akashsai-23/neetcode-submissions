class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        res = "".join(char for char in s if char.isalnum()).lower()
        if res == res[::-1]:
            return True
        return False


        