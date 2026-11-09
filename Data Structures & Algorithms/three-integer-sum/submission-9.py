class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # The goal is to return all possible combinations such that these three numbers
        # are in nums and equal to 0
        # Return an array where each element in an array of 3 numbers that total up to 0

        # Assumptions:
        # I can assume nums has at LEAST 3 numbers
        # If it has 0-2 numbers, return [] (not possible)
        # The values can be any number (as long as its possible in Python)
        # We do not have or return duplicate triplets
        
        # [0, 0, 0] => [[0, 0, 0]]
        # [0, 0, 1] => []
        # [0, 0, 0, 0] => [[0, 0, 0]]
        # [0, 0, 0, 1] => []
        # [-1, 0, 0, 1] => [[-1, 0, 1]]
        # [-1, -2, 0, 1] => [[-1, 0, 1]]
        # [-1, -2, 2, 1] => []
        # [-1, -2, 2, 1, 0] => [[-1, 0, 1], [-2, 0, 2]]

        # Interesting to note, some numbers can be used twice
        # We kind to have to try to "test every combination" with some sort of numbers
        # We can do like a for loop within a for loop
        # For this number, test every combination from left to right forward of it
        # We don't need to check behind SINCE theroetically, every number ahead of that 
        # was checked with this number

        # We can keep a left and right pointer, where r is the end of the list, and
        # l is the index after the number we are seeing if possible combinations exist
        # Then it's kind of like 2-pointer search
        # The important thing is that we have to do this from a "sorted" list
        # That way, 2-pointer "search" works, since we will know which pointer to decrease
        # Otherwise, we would have to continuously try every brute force combiation possible

        n = len(nums) 
        nums.sort()

        result = []
        for i in range(n):
            if nums[i] > 0:
                break
            l, r = i + 1, n - 1
            while l < r:
                sumNum = nums[l] + nums[r] + nums[i]
                if sumNum == 0:
                    if [nums[i], nums[l], nums[r]] not in result:
                        result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif sumNum > 0:
                    r -= 1
                else:
                    l += 1

        return result
