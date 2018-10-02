#include <vector>
using namespace std;


class Solution {
public:
    vector<int> constructArray(int n, int k) {
        vector<int> res(n, 0);

        // fill in the first part of the array and all the diff is 1
        for (int i = 0; i < n-k; i++){
            res[i] = i+1;
        }

        // the second part with k elements and k-1 diff
        for (int i = n-k; i < n; i++){
            // odd
            if ((i-n+k+1) & 1) {
                res[i] = n-k+(i-n+k+1);

            // even
            } else {
                res[i] = n - (i-n+k+1)/2+1;
            }
        }

        return res;
    }
};