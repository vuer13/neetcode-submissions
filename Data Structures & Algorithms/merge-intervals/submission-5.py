class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # So we want to return a list of intervals such that it is minimal
        # So no intervals overlap

        # We need some way to figure out, for this next given interval, does it overlap
        # Assumptions:
        # Intervals is a list of lists of length 2
        # All values are >= 0
        # All intervals are in a way such that left side < right side
        # Sanity check: len of return should be no greater than len of intervals

        # So I think the easiest way would be to sort some list of intervals
        # Than for each next interval, does it overlap with the previous
        # If it does, we can merge it
        # If it doesn't, this is out new "previous"

        intervals.sort(key=lambda x : x[0])

        result = []
        result.append(intervals[0])

        for start, end in intervals:
            lastEnd = result[-1][1]
            if lastEnd >= start:
                result[-1][1] = max(end, lastEnd)
            else:
                result.append([start, end])

        return result
