class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i

        end = 0
        length = 0
        result = []

        for i in range(len(s)):
            end = max(end, lastIndex[s[i]])
            length += 1

            if i == end:
                result.append(length)
                length = 0
            
        return result