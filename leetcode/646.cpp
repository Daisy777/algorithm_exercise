#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

class Solution {
private:
    void print(const vector<vector<int>>& vec) {
        for_each(vec.begin(), vec.end(), 
        [](vector<int> v) {
            int size = v.size();
            for (int i=0; i<size; i++) {
                cout << v[i];
            }
            cout << endl;
        });
    }
public:
    int findLongestChain(vector<vector<int>>& pairs) {
        int sizepairs = pairs.size();
        if (sizepairs==0) { return 0; }

        // same as the scheduling? - greedy
        sort(pairs.begin(), pairs.end(), [](const vector<int>& v1, const vector<int>& v2){ return v1[1] < v2[1]; });
        // print(pairs);
        int last = pairs[0][1];
        int max = 1;
        for (int i=1; i<sizepairs; i++) {
            if (pairs[i][0] <= last) { continue; }
            max += 1;
            last = pairs[i][1];
        }

        return max;
    }
};

// test
int main() {
    Solution sol;
    vector<int> vec1({1, 2});
    vector<int> vec2({2, 3});
    vector<int> vec3({3, 4});
    vector<vector<int>> vec({vec1, vec2, vec3});
    cout << sol.findLongestChain(vec);

    return 0;
}
