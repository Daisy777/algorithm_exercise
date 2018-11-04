#include <vector>
#include<iostream>
using namespace std::vector;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        for(vector<int>::iterator it = nums.begin(); it != nums.end(); it++) {
            *it = -*it;
        }
        return nums;
    

    }
};

int main() {
    int test[] = {-1, 0, 2, 1};
    vector<int> testV;
    testV.assign(test, test+sizeof(test)/sizeof(int));
    Solution solution = new Soluition();
    cout << solution.threeSum(testV) << std::endl;
}