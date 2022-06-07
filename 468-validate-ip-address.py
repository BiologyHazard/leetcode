class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP:
            l = queryIP.split('.')
            if not len(l) == 4:
                return 'Neither'
            for s in l:
                if not 1 <= len(s) <= 3:
                    return 'Neither'
                if not all(i in '0123456789' for i in s):
                    return 'Neither'
                if s != '0' and s[0] == '0':
                    return 'Neither'
                if not 0 <= int(s) < 256:
                    return 'Neither'
            return 'IPv4'
        elif ':' in queryIP:
            l = queryIP.split(':')
            if not len(l) == 8:
                return 'Neither'
            for s in l:
                if not 1 <= len(s) <= 4:
                    return 'Neither'
                if not all(i in '0123456789abcdefABCDEF' for i in s):
                    return 'Neither'
            return 'IPv6'
        return 'Neither'
