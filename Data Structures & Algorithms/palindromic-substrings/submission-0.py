class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        n = len(s)

        for i in range(n):
            result += self.countPali(s, i, i)
            result += self.countPali(s, i, i + 1)

        return result

    def countPali(self, s: str, i: int, j: int) -> int:
        n = len(s)
        result = 0

        while i >= 0 and j < n and s[i] == s[j]:
            result += 1
            i -= 1
            j += 1

        return result
