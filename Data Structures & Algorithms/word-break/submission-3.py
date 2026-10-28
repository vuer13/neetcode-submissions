class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        result = [False] * (n + 1)
        result[0] = True

        for i in range(1, n + 1):
            for word in wordDict:
                lenW = len(word)
                if i - lenW >= 0 and result[i - lenW] and s[i - lenW : i] == word:
                    result[i] = True

        return result[n]
