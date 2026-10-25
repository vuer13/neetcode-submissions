class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair : pair[0])
        lastEnd = intervals[0][1]

        result = 0
        for start, end in intervals[1:]:
            if start < lastEnd:
                result += 1
                lastEnd = min(lastEnd, end)
            else:
                lastEnd = end

        return result