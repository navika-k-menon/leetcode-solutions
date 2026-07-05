# Difficulty: Easy
# Topic: Linked List
#
# Approach:
# - Create a dummy node to simplify building the merged list.
# - Compare the current nodes of both linked lists.
# - Append the smaller node to the merged list.
# - Move the pointer of the list from which the node was taken.
# - Once one list is exhausted, append the remaining nodes of the other list.
# - Return the merged list starting from dummy.next.
#
# Time Complexity: O(n + m)
# Space Complexity: O(1)

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next