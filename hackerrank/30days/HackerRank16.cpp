#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

void convToNum(string str) {
    try {
        int num = stoi(str);
        cout << num << endl;
    } catch (invalid_argument e) {
        cout << "Bad String" << endl;
    }
}

int main(){
    string S;
    cin >> S;
    convToNum(S);
    return 0;
}

