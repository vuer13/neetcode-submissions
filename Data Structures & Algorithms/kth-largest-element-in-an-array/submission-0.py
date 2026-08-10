class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        listNums = []

        for num in nums:
            heapq.heappush(listNums, num)
            if len(listNums) > k:
                heapq.heappop(listNums)

        
        k_largest = heapq.heappop(listNums)

        return k_largest