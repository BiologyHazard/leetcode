# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p = head
        while p is not None:
            if hasattr(p, 'visited'):
                return True
            p.visited = True
            p = p.next
        return False
