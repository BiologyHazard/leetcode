from typing import List


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        longesttime = 0
        prevtime = 0
        lid = 1 << 15
        for sid, leavetime in logs:
            time = leavetime - prevtime
            if time > longesttime or (time == longesttime and sid < lid):
                longesttime = time
                lid = sid

            prevtime = leavetime
        return lid
