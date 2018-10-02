#include <vector>
using std::vector;

class Solution {
public:
    
    bool notDecreasing(vector<int>::iterator begin, vector<int>::size_type len){
        vector<int>::iterator middle = begin+(len-1)/2;

        if (len == 1) return true;
        
        if (*begin <= *middle && *middle <= *(begin + len-1) && *middle <= *(middle+1)) {
            return notDecreasing(begin, (len+1)/2) && notDecreasing(middle+1, len/2);
        }
        return false;
    }
    
    bool notIncreasing(vector<int>::iterator begin, vector<int>::size_type len){
        vector<int>::iterator middle = begin+(len-1)/2;

        if (len == 1) return true;
        
        if (*begin >= *middle && *middle >= *(begin + len-1) && *middle >= *(middle+1)) {
            return notIncreasing(begin, (len+1)/2) && notIncreasing(middle+1, len/2);
        }
        return false;
    }
    
    bool isMonotonic(vector<int>& A) {
        return notDecreasing(A.begin(), A.size()) || notIncreasing(A.begin(), A.size());
    }
};