#include <iostream>
#include <vector>
using namespace std;
# define MAX(a, b) ((a)>(b)?a:b)

class Solution {
public:
    int integerBreak(int n) {
        vector<int> vec(n+1);
        vec[1] = 1; // n > 2
        // integerBreak(n) <= n
        if(n==2) { return 1; }
        else { vec[2] = 1; }

        if(n==3) { return 2; }
        else  { vec[3] = 2; }

        if(n==4) { return 4; }
        else { vec[4] = 4; }

        for(int i=5; i<=n;i++) {
            // is there any math method to simplify this problem??
            int max(0);
            for(int j=1;j<=n/2; j++) {
                max = MAX(max, MAX(vec[j], j)*MAX(i-j, vec[i-j]));
            }
            vec[i] = max;
        }
        return vec[n];
    }
};

// test
int main() {
    Solution sol;
    cout << sol.integerBreak(10) << endl; // 36
}

