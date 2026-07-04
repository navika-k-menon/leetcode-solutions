# Difficulty: Easy
# Topic: Math
#
# Approach:
# - Negative numbers cannot be palindromes.
# - Store the original number.
# - Reverse the digits of the number using modulo (%) and integer division (//).
# - Compare the reversed number with the original.
#
# Time Complexity: O(log₁₀(n))
# Space Complexity: O(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original = x
        reverse = 0

        while x > 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x //= 10

        return original == reverse