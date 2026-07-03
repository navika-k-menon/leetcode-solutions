# Difficulty: Medium
# Topic: Sliding Window, Hash Table
#
# Approach:
# - Use a sliding window with two pointers.
# - Store the most recent index of each character in a hash map.
# - If a duplicate character is found within the current window,
#   move the left pointer just past its previous occurrence.
# - Update the maximum window length while traversing the string.
#
# Time Complexity: O(n)
# Space Complexity: O(min(n, m))
# where n is the length of the string and m is the character set size.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1

            char_index[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length