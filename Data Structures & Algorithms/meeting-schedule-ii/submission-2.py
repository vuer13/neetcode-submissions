"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        greedy = []
        for interval in intervals:
            greedy.append([interval.start, 1])
            greedy.append([interval.end, -1])

        greedy.sort(key=lambda x: (x[0], x[1]))

        curr = 0
        result = 0
        for _, value in greedy:
            curr += value
            result = max(result, curr)

        return result
