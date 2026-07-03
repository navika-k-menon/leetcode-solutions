# Difficulty: Medium
# Topic: Linked List
#
# Approach:
# - Traverse both linked lists simultaneously.
# - Add the corresponding digits along with any carry from the previous addition.
# - Create a new node for the current digit (total % 10).
# - Update the carry (total // 10).
# - Continue until both lists are exhausted and there is no remaining carry.
#
# Time Complexity: O(max(m, n))
# Space Complexity: O(max(m, n))

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            carry = total // 10
            current.next = ListNode(total % 10)

            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next  