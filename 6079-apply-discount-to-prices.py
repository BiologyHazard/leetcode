class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        l = sentence.split()
        for i, word in enumerate(l):
            if word[0] == '$':
                # for char in word[1:]:
                #     if char in range(10) or char == '.':
                s = word[1:]
                try:
                    price = float(s) * (1 - discount / 100)
                    l[i] = f'${price:.2f}'
                except:
                    pass
        return ' '.join(l)
