class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        # Up to character i, can you make a word out of it
        result = [False] * (n + 1)
        result[0] = True        # True for empty string

        for i in range(1, n + 1):
            for word in wordDict:
                lenWord = len(word)
                if i - lenWord >= 0 and s[i - lenWord:i] == word and result[i - lenWord]:
                    result[i] = True
                    break
                
        return result[n]
