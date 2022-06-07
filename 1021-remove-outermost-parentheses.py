class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        l = list(s)
        flag = [True for _ in s]
        c = 0
        for i, char in enumerate(s):
            if char == '(':
                c += 1
                if c == 1:
                    flag[i] = False
            else:
                c -= 1
                if c == 0:
                    flag[i] = False

        return ''.join(l[i] for i in range(len(s)) if flag[i])
