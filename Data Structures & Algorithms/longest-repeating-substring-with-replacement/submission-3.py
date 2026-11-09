class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # We need to find the longest substring such that it is only that character
        # with the exception that we can replace up to k characters in this string

        # Assumptions:
        # k is at least 0 and less than len(s)
        # if s is '', then we can return 0 (there is nothing)
        # I am also assuming that s is ONLY uppercase letters and nothing else

        # '', k = 0 => 0
        # 'A', k = 0 => 1
        # 'B', k = 0 => 1
        # 'B', k = 1 => 1
        # 'AA', k = 0 => 2
        # 'AB', k = 0 => 1
        # 'AB', k = 1 => 2
        # 'AB', k = 2 => 2
        # 'AAA', k = 0 => 3
        # 'ABB', k = 0 => 2
        # 'ABB', k = 1 => 3
        # 'ABC', k = 2 => 3
        # 'ABC', k = 1 => 2
        # 'ABC', k = 0 => 1
        # 'ABA', k = 0 => 1
        # 'ABA', k = 1 => 3
        # We want to essentially find in the string, some "substring" such that 
        # all the letters EXCEPT at most k of them are the same

        # We need some sort of sliding window I think
        # We need to keep track of the left value while we continue adding to the right as
        # as we can until we've reached out limit
        # That means for each substring/window, we need to find the MOST frequent 
        # character and also include the k swaps

        # What do we need to keep track of?
        # 1. frequency for each element in a particular window
        # - value of max freq in this window
        # 2. left value (we need to add to it if the restriction doesn't hold)
        # 3. longest length we've seen

        l = 0
        frequency_of_substring = {}
        longest_length = 0
        max_freq_in_window = 0

        for r in range(len(s)):
            frequency_of_substring[s[r]] = frequency_of_substring.get(s[r], 0) + 1
            max_freq_in_window = max(max_freq_in_window, frequency_of_substring[s[r]])
            while (r - l + 1) - max_freq_in_window > k:
                frequency_of_substring[s[l]] -= 1
                l += 1
            longest_length = max(longest_length, r - l + 1)

        return longest_length
            