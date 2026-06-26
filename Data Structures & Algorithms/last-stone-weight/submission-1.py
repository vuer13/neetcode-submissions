class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Sorts stones into a max_heap, O(nlogn)
        heapq.heapify_max(stones)

        # Best Case: remove both stones
        # Worst Case: remove one stone
        # Thus, O(n)
        while len(stones) > 1:
            # Pop top two stones in the heap: O(1)
            first_stone = heapq.heappop_max(stones)
            second_stone = heapq.heappop_max(stones)

            # Calculate the difference b/t the first and second stones
            difference = first_stone - second_stone
            
            # If a difference remains, push it back to stones
            # Otherwise, destroy both stones (or do nothing)
            if difference > 0:
                heapq.heappush_max(stones, difference)

        return stones[0] if len(stones) != 0 else 0