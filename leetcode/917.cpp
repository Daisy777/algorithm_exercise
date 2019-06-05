#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string reverseOnlyLetters(string S) {
        int begin=0, end=S.length()-1;
        int length = S.length();

        while(begin<end) {
            // find next char
            while(begin<length && !isalpha(S[begin])) { begin++; }
            while(end>-1 && !isalpha(S[end])) { end--; }

            if (begin>length-1 || end <0 || begin >= end) { break; }
            swap(S[begin], S[end]);
            begin++;
            end--;

        }

        return S;
        
    }
};

int main() {
    Solution sol;
    cout << sol.reverseOnlyLetters("ab-cd-") << endl; // dc-ba-
    cout << sol.reverseOnlyLetters("?6C40E") << endl; // ?6E40C
}