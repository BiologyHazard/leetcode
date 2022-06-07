class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        l = list(s)
        ans = 0
        flag = True
        while flag:
            for char in target:
                if char in l:
                    l.remove(char)
                else:
                    flag = False
                    break
            if flag:
                ans += 1
        return ans

