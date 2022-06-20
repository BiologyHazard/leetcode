class Solution:
    def greatestLetter(self, s: str) -> str:
        upper = [False for _ in range(26)]
        lower = [False for _ in range(26)]
        for char in s:
            if char.isupper():
                upper[ord(char) - ord('A')] = True
            else:
                lower[ord(char) - ord('a')] = True
        for i in reversed(range(26)):
            if upper[i] and lower[i]:
                return chr(i + ord('A'))
        return ''
