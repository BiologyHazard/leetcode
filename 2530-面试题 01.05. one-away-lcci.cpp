#include <string>
using namespace std;

class Solution
{
public:
    bool oneEditAway(string first, string second)
    {
        int n1 = first.size();
        int n2 = second.size();
        int i = 0;
        while (i < min(n1, n2) && first[i] == second[i])
            i += 1;
        int j = -1;
        while (-j <= min(n1, n2) && first[n1 + j] == second[n2 + j])
            j -= 1;
        return n1 + j + 1 - i <= 1 && n2 + j + 1 - i <= 1;
    }
};
