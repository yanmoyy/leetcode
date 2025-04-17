# 2130. Maximum Twin Sum of a Linked List

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        # find the middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second half of the list
        rev_head = self.reverseList(slow)
        # find the maximum twin sum
        max_twin_sum = 0
        while head and rev_head:
            max_twin_sum = max(max_twin_sum, head.val + rev_head.val)
            head = head.next
            rev_head = rev_head.next
        return max_twin_sum

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


class Solution2:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # store the values in a list
        values = []
        while head:
            values.append(head.val)
            head = head.next
        # find the maximum twin sum
        max_sum = 0
        for i in range(len(values) // 2):
            max_sum = max(max_sum, values[i] + values[len(values) - i - 1])
        return max_sum
