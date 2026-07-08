# Difficulty: Hard
# Topic: Array, Binary Search
#
# Approach:
# - Always binary search the smaller array.
# - Partition both arrays so that the total number of elements
#   on the left equals the total number on the right (or differs by one).
# - Check whether the partition is valid by comparing the largest values
#   on the left with the smallest values on the right.
# - If the partition is valid, compute the median.
# - Otherwise, adjust the binary search boundaries.
#
# Time Complexity: O(log(min(m, n)))
# Space Complexity: O(1)

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x = len(nums1)
        y = len(nums2)

        low = 0
        high = x

        while low <= high:

            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            maxLeftX = float("-inf") if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float("inf") if partitionX == x else nums1[partitionX]

            maxLeftY = float("-inf") if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float("inf") if partitionY == y else nums2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:

                if (x + y) % 2 == 0:
                    return (
                        max(maxLeftX, maxLeftY)
                        + min(minRightX, minRightY)
                    ) / 2

                return max(maxLeftX, maxLeftY)

            elif maxLeftX > minRightY:
                high = partitionX - 1

            else:
                low = partitionX + 1