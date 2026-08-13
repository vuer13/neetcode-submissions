class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charToIndex = {}
        left = 0
        longestSoFar = 0

        for r in range(len(s)):
            char = s[r]
            if char in charToIndex:
                left = max(charToIndex[char] + 1, left)
            longestSoFar = max(longestSoFar, r - left + 1)
            charToIndex[char] = r

        return longestSoFar