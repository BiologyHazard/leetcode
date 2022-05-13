def same(n1, n2) -> bool:
    if n1 is None and n2 is None:
        return True
    if n1 is None or n2 is None:
        return False
    if vals[n1] != vals[n2]:
        return False
    return same(lefts[n1], rights[n2]) and same(rights[n1], lefts[n2])


def count(n) -> int:
    if n is None:
        return 0
    return count(lefts[n]) + count(rights[n]) + 1


if __name__ == '__main__':
    n = int(input())
    vals = list(map(int, input().split()))
    lefts = []
    rights = []
    for i in range(n):
        l, r = map(int, input().split())
        if l == -1:
            l = None
        else:
            l = l - 1
        if r == -1:
            r = None
        else:
            r = r - 1
        lefts.append(l)
        rights.append(r)

    ans = 0
    for i in range(n):
        if same(i, i):
            ans = max(ans, count(i))
    print(ans)
