/*
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a
substring.
             
Author: ZHAO Zinan
Created Date: 4/4/2019 
*/

#include <iostream>
#include <string>
#include <bits/stdc++.h> 
#include <cmath>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int begin=0, end=0, maxlength=0; 
        int stringlen = s.length();
        if (stringlen==0) { return 0; }
        map<char, int> loc;
        while(end < stringlen) {
            map<char, int>::iterator f = loc.find(s[end]);
            if (f == loc.end() || f->second==-1){
                if (f->second==-1) {
                    f->second = end;
                } else { loc.insert(pair<int, int>(s[end], end)); }
                
                end++;
            } else {
                maxlength = max(end-begin, maxlength);
                int temp = loc[s[end]]+1;
                for(int i=begin; i<=loc[s[end]]; i++) {
                    std::map<char,int>::iterator it = loc.find(s[i]);
                    it->second = -1;
                }
                // for (map<char, int>::iterator itr = loc.begin(); itr != loc.end(); ++itr) { 
                //     cout << '\t' << itr->first 
                //         << '\t' << itr->second << '\n'; 
                // } 
                begin = temp;

                loc.find(s[end])->second = end;
                end++; 
            }
        }
        maxlength = max(end-begin, maxlength);

        return maxlength;
    }
};

int main() {
    Solution sol;
    cout << sol.lengthOfLongestSubstring("pwwkew") << endl; // 3
    cout << sol.lengthOfLongestSubstring("bbbbb") << endl;  // 1
    cout << sol.lengthOfLongestSubstring("abcabcbb") << endl; // 3
    cout << sol.lengthOfLongestSubstring(" ") << endl; // 1
    cout << sol.lengthOfLongestSubstring("aabaab!bb") << endl; // 3
}

