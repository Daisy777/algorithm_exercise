 /**
  * Author:    ZHAO Zinan
  Created: 12/08/2018

  841. Keys and Rooms
  https://leetcode.com/problems/keys-and-rooms/description/
  **/ 
#include <vector>
#include <set>
#include <queue>
#include <iostream>
using namespace std;

static int x=[](){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    return 0;
}();
class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int length = rooms.size();
        set<int> notVisited;
        for (int i=0; i<length; i++) {
            notVisited.insert(i);
        }
        queue<int> toVisite ({0});

        while(!toVisite.empty()) {
            int next = toVisite.front();
            toVisite.pop();
            notVisited.erase(next);

            for (vector<int>::iterator it=rooms[next].begin(); it!=rooms[next].end(); it++) {
                if (notVisited.find(*it) != notVisited.end()) {
                    toVisite.push(*it); 
                }
           }
       }

       return notVisited.empty();
    }
};
 