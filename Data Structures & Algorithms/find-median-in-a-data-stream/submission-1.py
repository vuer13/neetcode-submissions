class MedianFinder:

    def __init__(self):
        self.small = []
        self.big = []

    def addNum(self, num: int) -> None:
        if self.big and num > self.big[0]:
            heapq.heappush(self.big, num)
        else:
            heapq.heappush(self.small, -1 * num)

        if len(self.big) > len(self.small) + 1:
            heapq.heappush(self.small, -1 * heapq.heappop(self.big))
        elif len(self.small) > len(self.big) + 1:
            heapq.heappush(self.big, -1 * heapq.heappop(self.small))

    def findMedian(self) -> float:
        if len(self.big) > len(self.small):
            return self.big[0]
        elif len(self.small) > len(self.big):
            return -1 * self.small[0]
        else:
            return (self.big[0] + (-1 * self.small[0])) / 2
        