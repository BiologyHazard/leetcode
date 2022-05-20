class Solution:
    def isValid(self, s: str) -> bool:
        while True:
            if s == '':
                return True
            s_ = s.replace('abc', '')
            if s_ == s:
                return False
            s = s_
