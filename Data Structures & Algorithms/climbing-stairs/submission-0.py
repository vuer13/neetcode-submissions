class Solution:
    def climbStairs(self, n: int) -> int:
        temp = [0] * (n + 1)
        temp[0] = 0
        temp[1] = 1
        
        for i in range(2, n + 1):
            if temp[i - 1] + 1 == i:
                i1 = temp[i - 1] + 1
            if temp[i - 2] + 2 == i:
                i2 = temp[i - 2] + 2

            temp[i] = max(i1, i2)

        return temp[n]