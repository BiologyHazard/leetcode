# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p = None
        q = head
        while q is not None:
            r = q.next
            q.next = p
            p = q
            q = r
        return p
