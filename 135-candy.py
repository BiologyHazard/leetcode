from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        l = len(ratings)
        candycount = [1] * l
        for i in range(1, l):
            if ratings[i-1] < ratings[i]:
                candycount[i] = candycount[i-1] + 1
        for i in range(l-2, -1, -1):
            if ratings[i+1] < ratings[i]:
                candycount[i] = max(candycount[i], candycount[i+1] + 1)
        return sum(candycount)
