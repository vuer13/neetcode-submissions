class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        resultingIndex = 0
        resultingLength = 0

        for i in range(n):
            # Odd
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > resultingLength:
                    resultingLength = r - l + 1
                    resultingIndex = l
                l -= 1
                r += 1
            
            # Even
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > resultingLength:
                    resultingLength = r - l + 1
                    resultingIndex = l
                l -= 1
                r += 1

        return s[resultingIndex : resultingIndex + resultingLength]
