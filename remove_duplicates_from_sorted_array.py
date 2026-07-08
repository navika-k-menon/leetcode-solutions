# Difficulty: Easy
# Topic: Array, Two Pointers
#
# Approach:
# - Since the array is already sorted, duplicates appear next to each other.
# - Use one pointer to read through the array.
# - Use another pointer to track where the next unique element should be placed.
# - Whenever a new unique value is found, copy it to the write pointer and move the write pointer forward.
# - Return the number of unique elements.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        write = 1

        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1

        return write