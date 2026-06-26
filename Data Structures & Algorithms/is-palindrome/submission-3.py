class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1

        while start < end:
            while start < end and not self.alphaNum(s[start]):
                start += 1
            while start < end and not self.alphaNum(s[end]):
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))