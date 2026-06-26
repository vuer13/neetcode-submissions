class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = []
        stairs.append(1)
        stairs.append(2)

        for i in range(2, n):
            stairs.append(stairs[i - 1] + stairs[i-2])

        return stairs[n - 1]