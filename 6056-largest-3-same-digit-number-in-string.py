class Solution:
    def largestGoodInteger(self, num: str) -> str:
        a = [False for i in range(10)]
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                a[int(num[i])] = True
        for i in reversed(list(range(10))):
            if a[i]:
                return str(i)*3
        return ""
