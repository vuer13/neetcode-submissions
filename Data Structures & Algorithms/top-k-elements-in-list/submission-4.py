class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            freq[count].append(num)

        result = []
        for i in range(len(nums), -1, -1):
            for num in freq[i]:
                result.append(num)

            if len(result) == k:
                return result

        return None
