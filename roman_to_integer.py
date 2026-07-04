# Difficulty: Easy
# Topic: Hash Table, String
#
# Approach:
# - Store Roman numeral values in a dictionary.
# - Traverse the string from left to right.
# - If the current numeral is smaller than the next numeral,
#   subtract its value.
# - Otherwise, add its value.
# - The last numeral is always added.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        for i in range(len(s)):
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]

        return total