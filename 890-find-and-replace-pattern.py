from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            w2p = {}
            p2w = {}
            flag = True
            for i, wchar in enumerate(word):
                pchar = pattern[i]
                if wchar in w2p:
                    if w2p[wchar] != pchar:
                        flag = False
                        break
                else:
                    w2p[wchar] = pchar
                if pchar in p2w:
                    if p2w[pchar] != wchar:
                        flag = False
                        break
                else:
                    p2w[pchar] = wchar
            if flag:
                ans.append(word)
        return ans
