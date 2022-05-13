class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        product = 1
        for i in range(left, right + 1):
            product *= i
        product = str(product)
        c = 0
        n = len(product)
        while product[n-c-1] == '0':
            c += 1
        d = n - c
        if d <= 10:
            return product[:d] + 'e' + str(c)
        else:
            return product[:5] + '...' + product[d-5:d] + 'e' + str(c)
