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
        for i in intervals:
            greedy.append((i.start, 1))
            greedy.append((i.end, -1))

        greedy.sort(key=lambda x : (x[0], x[1]))

        cost = 0
        result = 0
        for _, state in greedy:
            cost += state
            result = max(result, cost)      # Return the max amount cost is at any time

        return result