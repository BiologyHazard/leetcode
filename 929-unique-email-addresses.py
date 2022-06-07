from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for email in emails:
            a, b = email.split('@')
            pos = a.find('+')
            if pos != -1:
                a = a[:pos]
            a = ''.join(a.split('.'))
            s.add(''.join([a, '@', b]))
        return len(s)
