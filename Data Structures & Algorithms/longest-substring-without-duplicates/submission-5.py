class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        lastSeen = {}
        longestLength = 0
        
        left = 0
        for right in range(n):
            char = s[right]
            if char in lastSeen:
                left = max(left, lastSeen[char] + 1)
            longestLength = max(right - left + 1, longestLength)
            lastSeen[char] = right

        return longestLength
