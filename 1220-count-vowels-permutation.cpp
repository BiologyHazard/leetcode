class Solution
{
public:
    int countVowelPermutation(int n)
    {
        const int M = 1e9 + 7;
        long a = 1, e = 1, i = 1, o = 1, u = 1;
        long aa = a, ee = e, ii = i, oo = o, uu = u;
        for (int j = 2; j <= n; j++)
        {
            aa = e + i + u;
            ee = a + i;
            ii = e + o;
            oo = i;
            uu = i + o;
            a = aa % M;
            e = ee % M;
            i = ii % M;
            o = oo % M;
            u = uu % M;
        }
        return (a + e + i + o + u) % M;
    }
};
