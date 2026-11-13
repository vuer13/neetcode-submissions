class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # We need to return the longest common subsequence in both words
        
        # Assumptions:
        # Obtain two strings that are valid
        # They contain any characters, doesn't matter
        # We can "delete" characters to obtain a subsequence, but we cannot insert
        
        # '', '' => 0
        # 'a', '' => 0
        # 'a', 'a' => 1
        # 'ab', 'a' => 1
        # 'ab', 'ab' => 2
        # 'abc', 'ab' => 2
        # 'abc', 'abc' => 3
        
        # '', '' => 0
        # 'a', '' => 0
        # '', 'a' => 0
        # 'a', 'a' => 1
        # 'ab', 'a' => 1 => j - 1
        # 'a', 'ac' => 1 => i - 1
        # 'ab', 'ac' => 1 => i, j
        # 'abc', 'ac' => 2

        # 'ba', 'a' => 1
        # 'ba', 'ab' => 1

        # Brute Force: Check every possible combination
        # Optimized: we need some pattern above
        # If the current two characters (at the ends match), it "adds" 1 to the count
        # Otherwise, we are taking some sort of previous count
        # Dynamic Programming would be good

        # Recursive Pattern:
        # For some i, j such that i < len(text1) and j < len(text2)
        # 1. if text1[i] == text2[j]: + 1 from some previous example (i don't know which one)
        # 2. otherwise: keep some previous count
        # What is this previous we are talking about?
        # - 1. text1[i] == text2[j] & we + 1: we must be looking at some i -1 and j -1 case
        # - 2. max out of the i - 1 and j - 1 case since the characters aren't equal, so
        # its the same number of combinations as previous

        m, n = len(text1), len(text2)
        subsequence_count = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            subsequence_count[i][0] = 1 if text1[i] == text2[0] else subsequence_count[i - 1][0]
        for j in range(n):
            subsequence_count[0][j] = 1 if text1[0] == text2[j] else subsequence_count[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                if text1[i] == text2[j]:
                    subsequence_count[i][j] = 1 + subsequence_count[i - 1][j - 1]
                else:
                    subsequence_count[i][j] = max(
                        subsequence_count[i - 1][j],
                        subsequence_count[i][j - 1]
                    )

        return subsequence_count[m - 1][n - 1]
