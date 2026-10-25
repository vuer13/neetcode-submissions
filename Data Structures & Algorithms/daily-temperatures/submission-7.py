class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        hotter = [0] * n

        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, index = stack.pop()
                hotter[index] = i - index
            stack.append((temp, i))

        return hotter