# Difficulty: Easy
# Topic: Stack, String
#
# Approach:
# - Use a stack to keep track of opening brackets.
# - Store matching bracket pairs in a dictionary.
# - Push every opening bracket onto the stack.
# - When a closing bracket is encountered, check whether it matches
#   the top element of the stack.
# - If it doesn't match or the stack is empty, return False.
# - At the end, the stack should be empty for the string to be valid.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0