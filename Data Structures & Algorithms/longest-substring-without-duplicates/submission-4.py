class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastIndex = {}
        result = 0
        l = 0

        n = len(s)

        for r in range(n):
            if s[r] in lastIndex:
                l = max(l, lastIndex[s[r]] + 1)
            result = max(result, r - l + 1)
            lastIndex[s[r]] = r

        return result