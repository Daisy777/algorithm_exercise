# Python
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        number = len(candies)
        kinds = len(set(candies)) 
        return min(kinds, number//2)

# // C++
# class Solution {
# public:
#     int distributeCandies(vector<int>& candies) {
#         int number = candies.size();
#         int kinds = set<int>(candies.begin(), candies.end()).size();
#         return min(kinds,number/2);
#     }
# };
