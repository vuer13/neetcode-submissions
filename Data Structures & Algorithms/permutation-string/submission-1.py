class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        n1 = len(s1)
        n2 = len(s2)

        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(n1):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        left = 0
        for right in range(n1, n2):
            if s1Count == s2Count:
                return True

            s2Count[ord(s2[right]) - ord('a')] += 1
            s2Count[ord(s2[left]) - ord('a')] -= 1

            left += 1

        return s1Count == s2Count
