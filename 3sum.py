# Difficulty: Medium
# Topic: Array, Two Pointers, Sorting
#
# Approach:
# - Sort the array.
# - Fix one number at a time.
# - Use two pointers to find two numbers that sum to the negative of the fixed number.
# - Skip duplicate values to avoid duplicate triplets.
#
# Time Complexity: O(n²)
# Space Complexity: O(1) (excluding the output list)

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1

                elif total > 0:
                    right -= 1

                else:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result