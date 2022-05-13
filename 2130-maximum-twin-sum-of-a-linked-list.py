from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l = []
        p = head
        while p is not None:
            l.append(p.val)
            p = p.next
        return max(l[i] + l[-i-1] for i in range(len(l) // 2))
