class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            anagram = [0] * 26
            for c in s:
                anagram[ord(c) - ord('a')] += 1
            anagrams[tuple(anagram)].append(s)

        return list(anagrams.values())
