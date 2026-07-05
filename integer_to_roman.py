# Difficulty: Medium
# Topic: String, Greedy
#
# Approach:
# - Store Roman numeral values and symbols in descending order.
# - Include subtractive combinations like IV, IX, XL, XC, CD and CM.
# - Repeatedly subtract the largest possible value from the number.
# - Append the corresponding Roman symbol each time until the number becomes zero.
#
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def intToRoman(self, num: int) -> str:
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        result = []

        for i in range(len(values)):
            while num >= values[i]:
                result.append(symbols[i])
                num -= values[i]

        return "".join(result)