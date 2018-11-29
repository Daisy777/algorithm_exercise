/**Author:    ZHAO Zinan
Created: 11/29/2018

455. Assign Cookies
https://leetcode.com/problems/assign-cookies/description/
**/ 
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

static int x=[](){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    return 0;
}();  

class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());

        vector<int>::iterator child = g.begin();
        vector<int>::iterator cookie = s.begin();
        int content = 0;

        while (cookie != s.end()) {
            if (child == g.end()) {
                return content;
            }
            if (*cookie >= *child) {
                content ++;
                child ++;
                cookie ++;
            } else {
                cookie ++;
            }
        }

        return content;
    }
};


// test
int main(){
    Solution solution;
    // int garr[] = {1, 2, 3};
    // vector<int> g (garr, garr+sizeof(garr)/sizeof(int));

    // int sarr[] = {1, 1};
    // vector<int> s (sarr, sarr+sizeof(sarr)/sizeof(int));

    // cout << solution.findContentChildren(g, s);

    int garr[] = {1, 2};
    vector<int> g (garr, garr+sizeof(garr)/sizeof(int));

    int sarr[] = {1, 2, 3};
    vector<int> s (sarr, sarr+sizeof(sarr)/sizeof(int));

    cout << solution.findContentChildren(g, s);

    return 0;
}