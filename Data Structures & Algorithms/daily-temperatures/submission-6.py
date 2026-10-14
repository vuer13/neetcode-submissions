class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        stack = []
        result = [0] * n

        for i, n in enumerate(temperatures):
            while stack and stack[-1][1] < n:
                index, _ = stack.pop()
                days = i - index
                result[index] = days
            stack.append((i, n))

        return result