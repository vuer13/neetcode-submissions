class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # We need to find out if two strings can "interleave" together somehow
        # Order must be preserved somehow
        
        # Assumptions:
        # 1. s1 and s2 are both valid strings containing only lowercase letters
        # 2. len(s1) and len(s2) make len(s3) -> if not, return False right away
        # 3. Order must be preserved in both s1 and s2 to make s3

        # Edge cases
        # See number 2 in assumptions
        # s1 = s3 if s2 is "" and vice versa
        
        # Examples:
        # s1, s2, s3
        # "", "", "" => True

        # Edge cases!!!
        # "a", "", "" => False
        # "a", "", "a" => True
        # "", "a", "a" => True
        # "ab", "", "ab" => True
        # "", "ac", "ab" => False

        # "c", "", "a" => False
        # "cb", "", "ab" => False

        # "a", "b", "ab" => True
        # "b", "a", "ab" => True
        # "ac", "b", "abc" => True
        # "cb", "a", "abc" => False

        # "a", "b", "ab" => True
        # "ac", "b", "abc" => True
        # "a", "bc", "ab" => True
        # "ac", "bc", "abc" => False

        # Observations:
        # 1. If previously it was False, adding an additional letter will not make it True (edge case)
        # 2. We can interleave such that s1 goes first or s2 goes first
        # 3. Order must be preserved when interleaving, so we have to iterate it order
        # 4. Everytime we add some sort of letter from either s1[i] or s2[j], it must equal the i + j index of s3
        # - or something like that
        # 5. That makes me think if previously we are interleaving, when we add some letter that is equivalent based on 4.
        # we just use a prior result to determine if it is interleaving

        # Since we need some sort of prior result, we likely need Dynamic Programming (2-D)
        # Why 2-D => we have 2 strings to interleave (ie. two things to consider)

        if len(s1) + len(s2) != len(s3):
            return False

        m, n = len(s1), len(s2)
        interleaving = [False for _ in range(n + 1)]
        interleaving[0] = True

        for j in range(1, n + 1):
            interleaving[j] = interleaving[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            interleaving[0] = interleaving[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, n + 1):
                take1 = interleaving[j] and s1[i - 1] == s3[i + j - 1]
                take2 = interleaving[j - 1] and s2[j - 1] == s3[i + j - 1]
                interleaving[j] = take1 or take2

        return interleaving[n]
