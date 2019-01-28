/**
 * Author:    ZHAO Zinan
 * Created: 01/28/2019
 * 
 * 551. Student Attendance Record I
 * **/ 
#include <string>
#include <map>
#include <iostream>
#include <algorithm>

class Solution {
public:
    bool checkRecord(std::string s) {
        std::map<char, int> counter;
        bool last_L = false;
        int max_L = 0;

        for(char& c : s) {
            if (c=='L') {
                if (last_L) {
                    counter['L'] ++;
                } else {
                    max_L = std::max(max_L, counter['L']);
                    counter['L'] = 1;
                    last_L = true;
                }
            } else {
                counter[c] ++;
                last_L = false;
            }
        }
        max_L = std::max(max_L, counter['L']);
        // for (auto pair: counter) {
        //     std::cout << pair.first << " " << pair.second << std::endl;
        // }
        if (max_L <= 2 && counter['A'] <= 1) {
            return true;
        }
        return false;
    }
};
static const auto io_sync_off = []()
{
    // turn off sync
    std::ios::sync_with_stdio(false);
    // untie in/out streams
    std::cin.tie(nullptr);
    return nullptr;
}();

int main() {
    Solution sol = Solution();
    std::cout << sol.checkRecord("LALL") << std::endl;
    std::cout << sol.checkRecord("LLLALL") << std::endl;
    std::cout << sol.checkRecord("PPALLL") << std::endl;
}