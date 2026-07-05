# Difficulty: Medium
# Topic: Array, Sorting, Two Pointers
#
# Approach:
# - Sort the array.
# - Fix one number at a time.
# - Use two pointers to find the sum closest to the target.
# - Update the closest sum whenever a better one is found.
# - Move pointers based on whether the current sum is smaller or larger than the target.
#
# Time Complexity: O(n²)
# Space Complexity: O(1)

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum

                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum

        return closest