class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # We are looking for the area b/t two bars that contains the most "water"
        # Given an array of numbers

        # Assumptions:
        # 1. The array has at least 2 values in it, otherwise return 0 (or None)
        # 2. Each number in the array is at least 0

        # [0, 2] => 0
        # [1, 2] => 1
        # [2, 2] => 2
        # [3, 2] => 2
        # We see from these examples above, what limits us is the "shortest" height

        # [1, 2, 3] => 1 x 2, 1 x 1, 2 x 1 => 2
        # [2, 1, 3] => 2 x 2, 2 x 1, 3 x 1 => 4
        # The limiting factor is the shortest height
        # When we encounter a "short" height, what can we do?
        # We can test another height essentially
        # What we do know, is that if you use this short height 
        # (where the width is at its max), then, anything at smaller widths has to
        # be smaller, so we can kind of check the "next" possible height at a smaller width
        # to see if that can create a potentially bigger area
        # If that's smaller, using that previous height for this next height based on the 
        # variant above, would've not helped anyways as well
        
        # We can start by looking at the biggest width and see the area
        # Whatever is shortest, we can move that bar in by 1
        # This decreases the width by 1 (guaranteed), however
        # 1. if the bar is taller, we will likely get the same or bigger area
        # 2. if the bar is shorter, than yes, the area is smaller, but the area would've 
        # been smaller anyways since we decreased width and lost the "taller bar"
        # 3. height is the same, area decreases, literally nothing changes

        # This above sounds like a 2-pointer approach
        # l += 1 or r -= 1 depending on the shorter bar
        # Check area everytime we make a change

        area = 0
        l, r = 0, len(heights) - 1

        while l < r:
            currArea = (r - l) * min(heights[l], heights[r])
            area = max(area, currArea)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return area
