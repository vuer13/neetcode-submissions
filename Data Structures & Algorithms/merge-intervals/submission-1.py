class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair : pair[0])
        result = [intervals[0]]

        for start, end in intervals:
            lastEnd = result[-1][1]

            # Since we sorted intervals earlier, we know for a fact that
            # start is in ascending order, thus it is a fact that each start
            # is at least at minimum the start before

            # We really need to see if start starts before the previous lastEnd
            if start <= lastEnd:
                result[-1][1] = max(end, lastEnd)
            else:
                result.append([start, end])

        return result