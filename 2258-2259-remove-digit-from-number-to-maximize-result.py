class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        psb_anss = []
        for i, char in enumerate(number):
            if char == digit:
                psb_anss.append(number[:i] + number[i+1:])
        return max(psb_anss)
