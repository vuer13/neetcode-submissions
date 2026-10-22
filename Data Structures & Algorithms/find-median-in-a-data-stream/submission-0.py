class MedianFinder:

    def __init__(self):
        # All heaps are minHeaps in Python
        self.smallHeap = []
        self.bigHeap = []   

    def addNum(self, num: int) -> None:
        if self.bigHeap and num > self.bigHeap[0]:
            heapq.heappush(self.bigHeap, num)
        else:
            heapq.heappush(self.smallHeap, num * -1)

        # Rebalance
        if len(self.smallHeap) > len(self.bigHeap) + 1:
            value = heapq.heappop(self.smallHeap) * -1
            heapq.heappush(self.bigHeap, value)
        elif len(self.bigHeap) > len(self.smallHeap) + 1:
            value = heapq.heappop(self.bigHeap)
            heapq.heappush(self.smallHeap, value * -1)

    def findMedian(self) -> float:
        if len(self.smallHeap) > len(self.bigHeap):
            return self.smallHeap[0] * -1
        elif len(self.bigHeap) > len(self.smallHeap):
            return self.bigHeap[0]
        else:
            return ((self.smallHeap[0] * -1) + (self.bigHeap[0])) / 2
        