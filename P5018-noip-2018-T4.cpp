#include <iostream>
using namespace std;
struct node
{
    long long l, r, val;
} bt[1000002];
bool same(long long now1, long long now2)
{
    if (now1 == -1 && now2 == -1)
        return true;
    if (now2 == -1 || now1 == -1)
        return false;
    if (bt[now1].val != bt[now2].val)
        return false;
    return same(bt[now1].l, bt[now2].r) && same(bt[now1].r, bt[now2].l);
}
int count(long long now)
{
    if (now == -1)
        return 0;
    return count(bt[now].l) + count(bt[now].r) + 1;
}
int main()
{
    int n, ans = 0;
    cin >> n;
    for (int i = 1; i <= n; i++)
        cin >> bt[i].val;
    for (int i = 1; i <= n; i++)
        cin >> bt[i].l >> bt[i].r;
    for (int i = 1; i <= n; i++)
        if (same(i, i))
            ans = max(ans, count(i));
    cout << ans;
    return 0;
}
