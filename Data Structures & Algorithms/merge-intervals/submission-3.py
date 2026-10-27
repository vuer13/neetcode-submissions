class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        result.append(intervals[0])

        for interval in intervals:
            start = interval[0]
            lastEnd = result[-1][1]

            if start <= lastEnd:
                result[-1][1] = max(interval[1], lastEnd)
            else:
                result.append(interval)


        return result
