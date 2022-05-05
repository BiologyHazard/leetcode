class Solution:
    def countLargestGroup(self, n: int) -> int:
        count = [0 for i in range(40)]
        for i in range(1, n+1):
            count[sum(map(int, str(i)))] += 1
        return count.count(max(count))
