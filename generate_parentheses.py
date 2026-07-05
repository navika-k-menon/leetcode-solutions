# Difficulty: Medium
# Topic: Backtracking
#
# Approach:
# - Build the parentheses string one character at a time.
# - Add an opening bracket if we still have some remaining.
# - Add a closing bracket only if it won't make the sequence invalid.
# - When the string reaches length 2 * n, store it as a valid answer.
#
# Time Complexity: O(4ⁿ / √n)
# Space Complexity: O(n)

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(current, open_count, close_count):
            if len(current) == 2 * n:
                result.append(current)
                return

            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)

        return result