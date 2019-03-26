#include<iostream>
#include<vector>
using namespace std;
#define min(a, b) (a<b?a:b)

void operator+=(vector<int> &a, const vector<int> &b) {
    for (int i = 0; i < a.size(); i++)
        a[i] += b[i];
}

void operator-=(vector<int> &a, const vector<int> &b) {
    for (int i = 0; i < a.size(); i++)
        a[i] -= b[i];
}

bool operator<(const vector<int> &a, const int &n) {
    for (int i : a)
        if (i < n)
            return true;
    return false;
}

int operator*(const vector<int> &a, const vector<int> &b) {
    int res = 0;
    for (int i = 0; i < a.size(); i++)
        res += a[i] * b[i];
    return res;
}

class Solution {
public:
    int shoppingOffers(vector<int>& price, vector<vector<int>>& special, vector<int>& needs, int cost=0) {
        // dfs
        if (needs < 0) { return INT_MAX; } // INT8_MAX returns wrong answer...
        int m = price*needs + cost;

        for(auto &s: special) {
            if (cost + s.back() >= m) { continue; }
            needs -= s;
            m = min(m, shoppingOffers(price, special, needs, cost+s.back()));
            needs += s;
        }

        return m;
    }
};

static const auto io_sync_off = [](){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    return nullptr;
}();



int main() {
    Solution sol;
    vector<int> price1({2, 5});
    vector<int> special11({3, 0, 5});
    vector<int> special12({1, 2, 10});
    vector<vector<int>> special1({special11, special12});
    vector<int> needs1({3, 2});

    cout << sol.shoppingOffers(price1, special1, needs1);

    return 0;
}