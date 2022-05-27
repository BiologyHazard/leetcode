#include <vector>

using namespace std;

class Solution
{
public:
    int maxTurbulenceSize(vector<int> &arr)
    {
        int n = arr.size();
        int dp = 1;
        int cmp = 0;
        int ans = 1;
        for (int i = 1; i < n; ++i)
        {
            if (cmp == 1 && arr[i - 1] < arr[i])
            {
                dp += 1;
                cmp = -1;
            }
            else if (cmp == -1 && arr[i - 1] > arr[i])
            {
                dp += 1;
                cmp = 1;
            }
            else
            {
                if (arr[i - 1] < arr[i])
                {
                    dp = 2;
                    cmp = -1;
                }
                else if (arr[i - 1] > arr[i])
                {
                    dp = 2;
                    cmp = 1;
                }
                else
                {
                    dp = 1;
                    cmp = 0;
                }
            }
            ans = max(ans, dp);
        }
        return ans;
    }
};
