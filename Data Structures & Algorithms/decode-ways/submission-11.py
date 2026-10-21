class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        result = [0] * (n + 1)
        result[0] = 1

        for i in range(1, n + 1):
            if s[i - 1] != '0':
                result[i] += result[i - 1]

            if i >= 2 and 10 <= int(s[i - 2:i]) <= 26:
                result[i] += result[i - 2]

        return result[n]
