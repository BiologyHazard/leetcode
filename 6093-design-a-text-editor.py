class ListNode:
    def __init__(self, val: str | None = None, prev: 'ListNode' | None = None, next: 'ListNode' | None = None):
        self.val = val
        self.prev = prev
        self.next = next


class TextEditor:
    # def print(self):
    #     p = self.head.next
    #     while p.next is not None:
    #         print(p.val, end='')
    #         p = p.next
    #     print()

    def __init__(self):
        # self.text = []
        # self.cursor = 0
        self.head = ListNode()
        p = ListNode(None, self.head, None)
        self.head.next = p
        self.cursor = p

    def addText(self, text: str) -> None:
        # r = self.text[self.cursor:]
        # del self.text[self.cursor:]
        # self.text.extend(list(text))
        # self.text.extend(r)
        # self.cursor += len(text)
        n = len(text)
        for i in range(n):
            p = ListNode(text[i], self.cursor.prev, self.cursor)
            self.cursor.prev.next = p
            self.cursor.prev = p
        # self.print()

    def deleteText(self, k: int) -> int:
        # lb = max(0, self.cursor - k)
        # del self.text[lb:self.cursor]
        # ret = self.cursor - lb
        # self.cursor = lb
        # return ret
        ans = 0
        while ans < k and self.cursor.prev != self.head:
            ans += 1
            self.cursor.prev = self.cursor.prev.prev
            self.cursor.prev.next = self.cursor
        # self.print()
        return ans

    def cursorLeft(self, k: int) -> str:
        # self.cursor = max(0, self.cursor - k)
        # lb = max(0, self.cursor - 10)
        # return ''.join(self.text[lb:self.cursor])
        while k > 0 and self.cursor.prev != self.head:
            k -= 1
            self.cursor = self.cursor.prev
        ans = []
        n = 0
        p = self.cursor.prev
        while n < 10 and p != self.head:
            n += 1
            ans.append(p.val)
            p = p.prev
        return ''.join(reversed(ans))

    def cursorRight(self, k: int) -> str:
        # self.cursor = min(len(self.text), self.cursor + k)
        # lb = max(0, self.cursor - 10)
        # return ''.join(self.text[lb:self.cursor])
        while k > 0 and self.cursor.next != None:
            k -= 1
            self.cursor = self.cursor.next
        ans = []
        n = 0
        p = self.cursor.prev
        while n < 10 and p != self.head:
            n += 1
            ans.append(p.val)
            p = p.prev
        return ''.join(reversed(ans))


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
