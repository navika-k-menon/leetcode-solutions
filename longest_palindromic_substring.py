# Difficulty: Medium
# Topic: String, Two Pointers
#
# Approach:
# - Every palindrome has a center.
# - For each character, expand around it to find the longest odd-length palindrome.
# - Also expand between the current and next character to find the longest even-length palindrome.
# - Keep track of the longest palindrome found.
#
# Time Complexity: O(n²)
# Space Complexity: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) < 2:
            return s

        start = 0
        end = 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return right - left - 1

        for i in range(len(s)):

            odd = expand(i, i)

            even = expand(i, i + 1)

            length = max(odd, even)

            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2

        return s[start:end + 1]