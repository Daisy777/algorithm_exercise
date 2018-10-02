#include<vector>
using std::vector;

#include <numeric>
#include <algorithm>

class Solution {
public:
    vector<int> fairCandySwap(vector<int>& A, vector<int>& B) {
        int sumA = std::accumulate(A.begin(), A.end(), 0);
        int sumB = std::accumulate(B.begin(), B.end(), 0);

        int diff = sumA - sumB;

        for (vector<int>::iterator it = A.begin(); it != A.end(); ++it){
            if (std::find(B.begin(), B.end(), *it-diff/2) != B.end()) {
                vector<int> result;
                result.push_back(*it);
                result.push_back(*it-diff/2);

                return result;
            }
        }  
    }
};