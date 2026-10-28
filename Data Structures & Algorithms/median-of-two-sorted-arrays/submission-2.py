class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        total_left = (m + n + 1) // 2
        left, right = 0, m

        while left <= right:
            cut1 = (right + left) // 2
            cut2 = total_left - cut1

            l1 = float("-infinity") if cut1 == 0 else nums1[cut1 - 1]
            r1 = float("infinity") if cut1 == m else nums1[cut1]
            l2 = float("-infinity") if cut2 == 0 else nums2[cut2 - 1]
            r2 = float("infinity") if cut2 == n else nums2[cut2]

            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2 == 1:
                    return max(l1, l2)
                else:
                    return (min(r1, r2) + max(l1, l2)) / 2
            elif l1 > r2:
                right = cut1 - 1
            else:
                left = cut1 + 1

        return None
