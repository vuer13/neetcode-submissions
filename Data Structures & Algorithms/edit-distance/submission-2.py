class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # We need to find the MINIMUM number of combinations to make such that we can make word1 equal word2

        # Assumptions
        # Both word1 and word2 are valid strings
        # Their lengths can be anything from 0 to max number
        
        # Brute Force:
        # Literally go through word1 and find every possible combination
        # Exponential time likely

        # Small examples:
        # "", "" => 0
        # "a", "" => 1
        # "ab", "" => 2
        
        # "", "" => 0
        # "", "a" => 1
        # "", "ab" => 2

        # "", "a" => 1
        # "", "" => 0
        # "a", "a" => 0
        # "b", "a" => 1
        # "ab", "a" => 1
        # "bc", "a" => 2
        # "ca", "a" => 1

        # "", "" => 0
        # "b", "a" => 1

        # "a", "a" => 0
        # "ab", "a" => 1

        # "a", "a" => 0
        # "a", "ab" => 1

        # Observations: 
        # If letters are the same, the number of operations is less than if they weren't
        # For example, a and a is 0, but b and a is 1 
        # ab and a is 1 but bc and a is 2
        # This can indicate that we may need to to an equivalent letter check b/t the two
        # Whenever we add a letter, that's an additional operation
        # Whenever we need to remove a letter, that's also an additional operation
        # We need some way of keep track of previous operations 

        # Dynamic Programming
        # Each square can represent the minimum number of operations of text1[:i] to get to text2[:j]
        # if word1[i] == word2[j]: array[i - 1][j - 1]
        # otherwise: min(array[i - 1][j - 1] + 1, array[i - 1][j] + 1, array[i][j - 1] + 1)

        m, n = len(word1), len(word2)
        distances = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            distances[i][0] = distances[i - 1][0] + 1
        for j in range(1, n + 1):
            distances[0][j] = distances[0][j - 1] + 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    distances[i][j] = distances[i - 1][j - 1]
                else:
                    distances[i][j] = min(distances[i - 1][j], distances[i][j - 1], distances[i - 1][j - 1]) + 1

        return distances[m][n]
