class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        s2Running = [0] * 26

        for char in s1:
            s1Count[ord(char) - ord('a')] += 1

        l = 0
        for char in s2[:len(s1)]:
            s2Running[ord(char) - ord('a')] += 1
        
        if s2Running == s1Count:
            return True

        for r in range(len(s1), len(s2)):
            s2Running[ord(s2[l]) - ord('a')] -= 1
            s2Running[ord(s2[r]) - ord('a')] += 1
            if s2Running == s1Count:
                return True
            l += 1

        return False
