class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, x in enumerate(s):
            lastIndex[x] = i

        size = 0
        end = 0
        result = []
        for i, x in enumerate(s):
            size += 1
            end = max(end, lastIndex[x])

            if i == end:
                result.append(size)
                size = 0
        
        return result