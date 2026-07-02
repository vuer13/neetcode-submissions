class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}

        lenS = len(s)
        lenT = len(t)

        if lenS != lenT:
            return False

        for i in range(lenS):
            s_hash[s[i]] = 1 + s_hash.get(s[i], 0)
            t_hash[t[i]] = 1 + t_hash.get(t[i], 0)

        return s_hash == t_hash