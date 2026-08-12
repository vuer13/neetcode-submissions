class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        stack = []

        for i, n in enumerate(temperatures):
            while stack and stack[-1][1] < n:
                index = stack[-1][0]
                differenceInDays = i - index
                result[index] = differenceInDays
                stack.pop()
            stack.append((i, n))

        return result