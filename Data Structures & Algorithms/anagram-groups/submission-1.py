class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            anagram = [0] * 26 # our "key"
            for c in s:
                index = ord(c) - ord('a') # find index normalized from 'a'
                anagram[index] += 1
            anagrams[tuple(anagram)].append(s)

        return list(anagrams.values())
