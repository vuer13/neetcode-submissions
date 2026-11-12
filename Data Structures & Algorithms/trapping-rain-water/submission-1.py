class Solution:
    def trap(self, height: List[int]) -> int:
        # For this "container" with random spikes, we need to return the maximum water that can
        # be stuck between these bars (starting at 0 all the way to n)

        # Assumptions:
        # 1. water cannot be stuck between the ends, it must be stuck b/t two heights 
        # specified in height
        # 2. all values in height are > 0, other invalid
        
        # Examples:
        # [] => 0 b/c we cannot return anything
        # [0] => 0 since there is no "water" b/t two bars
        # [1, 2] => 0 since there is still no "water" b/t two bars
        # [3, 1, 2] => 1 since water "sits" on index 1, and we have height 3/2 (effectively 2 and 1)
        # [1, 2, 3] => 0 since no water is trapped
        # [3, 0, 1, 2] => 3 (0, 2, 1, 0)
        # [3, 0, 2, 0, 1] => 3 (0, 2, 0, 1, 0)
        # [3, 0, 0, 0, 1] => 3 (0, 1, 1, 1, 0)
        # [3, 0, 1, 0, 2] => 5 (0, 2, 1, 2, 0)
        # [3, 0, 4, 1, 2] => 4 (0, 3, 0, 1, 0)
        # Observation, we are limited by the "smallest" thing on the left or right
        # So, i think we can look at index 2 to n-2 and see, what is limiting the height at each index
        # We need to add water everytime (probably height[index] - minimum max on the left or right)
        
        # I think we can initialize a left and right pointer
        # We can also initialize a leftMax and rightMax
        # From there, we can move the left pointer or right pointer
        # - at each position, find the (height[index] - minimum max on the left or right)
        # - add it to a running total
        # We also need to update the max height everytime somehow (probably at each iteration, check is this height a new maximum)
        
        # What could this algorithm look like
        # 2 pointers:
        # One tracks left, one tracks right
        # Calculate height[index] - minimum max on the left or right
        # We move the side with the minimum max height since that will always limit us, it doesn't matter what is on the other side
        # ie. technically, directly on the other side could be a smaller height (ie. [2, 0, 0, 1])
        # But here, since 1 is the minimal height, we don't really care what's on the other side since we know it will at least 
        # bounded here by something (whether its 0, 2, 2, whatever) since it HAS TO BE 1 here
        
        if len(height) < 3:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]

        water = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])           # Check here to see, is this taller
                water += (leftMax - height[l])              # If it is taller, not adding anything
                                                            # If not taller, we are adding water based on the minimal height
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                water += (rightMax - height[r])

        return water
