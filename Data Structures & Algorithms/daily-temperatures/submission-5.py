class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        stack = []

        for i, n in enumerate(temperatures):
            while stack and stack[-1][1] < n:
                index, _ = stack.pop()
                differenceInDays = i - index
                result[index] = differenceInDays
            stack.append((i, n))

        return result