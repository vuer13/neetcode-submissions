class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Assumptions: k > 0
        # len(set(nums)) >= k 
        # [], k = 1 => INVALID
        # [1], k = 1 => 1
        # [1, 2], k = 1 => 1 or 2 (Doesn't matter)
        # [1, 1], k = 1 => 1
        # [1, 2], k = 2 => [1, 2]
        # [1, 1], k = 1 => 1
        # [1, 1, 1], k = 1 => 1
        # [1, 1, 2], k = 1 => 1
        # [2, 1, 2], k = 1 => 2
        # [1, 1, 2], k = 2 => [1, 2]
        # [2, 1, 2], k = 2 => [1, 2]

        # We need:
        # Number of each element in nums
        # We need to sort that somehow, someway to get the top k elements

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        n = len(nums)
        frequency = [[] for _ in range(n + 1)]
        for num, freq in count.items():
            frequency[freq].append(num)

        result = []
        for i in range(len(nums), -1, -1):
            for num in frequency[i]:
                result.append(num)

            if len(result) == k:
                return result

        return None
