class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        # Stores number:count pairings

        heap = []
        for num in counts.keys():
            heapq.heappush(heap, (counts[num], num)) # Order based on the counts, with num on the side
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for _, num in heap:
            result.append(num)

        return result