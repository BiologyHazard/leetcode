class Solution:
    def canChange(self, start: str, target: str) -> bool:
        sc = []
        sp = []
        tc = []
        tp = []
        for i, char in enumerate(start):
            if char in ('L', 'R'):
                sc.append(char)
                sp.append(i)
        for i, char in enumerate(target):
            if char in ('L', 'R'):
                tc.append(char)
                tp.append(i)

        if sc != tc:
            return False

        for i in range(len(sc)):
            if sc[i] == 'L':
                if sp[i] < tp[i]:
                    return False
            else:
                if sp[i] > tp[i]:
                    return False
        return True
