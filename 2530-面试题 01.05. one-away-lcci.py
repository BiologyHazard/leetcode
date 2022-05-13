class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        n1, n2 = len(first), len(second)
        i = 0
        while i < min(n1, n2) and first[i] == second[i]:
            i += 1
        j = -1
        while -j <= min(n1, n2) and first[j] == second[j]:
            j -= 1
        # a = first[i:n1+j+1]
        # b = second[i:n2+j+1]
        # return len(a) <= 1 and len(b) <= 1
        return n1+j+1 - i <= 1 and n2+j+1 - i <=1
