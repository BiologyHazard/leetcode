# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        p = head
        carry = 0
        while l1 or l2 or carry:
            x1 = l1.val if l1 else 0
            x2 = l2.val if l2 else 0
            p.next = ListNode()
            p = p.next
            p.val = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head.next


if __name__ == '__main__':
    l1 = ListNode(2, ListNode(1))
    l2 = ListNode(4, ListNode(3))
    ans = Solution().addTwoNumbers(l1, l2)
    while ans:
        print(ans.val)
        ans = ans.next
