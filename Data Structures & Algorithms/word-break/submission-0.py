class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        # Each position represents if up until that position does it break
        # Does not include i
        # So for i = 1, we really are just looking at one character, not position 1
        word_break = [False for _ in range(n + 1)]
        word_break[0] = True

        for i in range(1, n + 1):
            for word in wordDict:
                start = i - len(word)

                if start >= 0 and word_break[start] and s[start:i] == word:
                    word_break[i] = True
                    break

        return word_break[n]
