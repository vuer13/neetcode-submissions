class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longestLength = 0
        l = 0
        
        frequency = {}
        maxFreq = 0

        for r in range(len(s)):
            frequency[s[r]] = frequency.get(s[r], 0) + 1
            maxFreq = max(maxFreq, frequency[s[r]])

            while (r - l + 1) - maxFreq > k:
                frequency[s[l]] -= 1
                l += 1

            longestLength = max(longestLength, r - l + 1)

        return longestLength
            