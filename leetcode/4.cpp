#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int size1 = nums1.size();
        int size2 = nums2.size();

        if (size1 > size2) {
            swap(size1, size2);
            nums1.swap(nums2);
        }

        // edge case
        if (size2==0) throw "Invalid array";

        int halfsize = (size1+size2+1)/2;
        int imax=size1, imin=0;
        bool complete = false;
        int i, j;

        while(!complete) {
            i=(imax+imin)/2;
            j=halfsize-i;
            if (i < size1 && nums2[j-1] > nums1[i]) {
                imin = i+1;
            } else if (i>0 && nums2[j] < nums1[i-1]) { 
                imax = i-1; 
            } else {
                complete = true;
            }
        }        
        int left, right;
        if (i==0) { left = nums2[j-1]; }
        else if (j==0) { left = nums1[i-1]; }
        else { left = max(nums2[j-1], nums1[i-1]); }

        if ((size1+size2)%2==1) { return double(left);}

        // Note that if the boundary is set on the right, it will == size
        // instead of size-1
        if (i==size1) { right = nums2[j]; }
        else if (j==size2) { right = nums1[i]; }
        else { right = min(nums2[j], nums1[i]); }

        return (left+right)/2.0;
    }
};

int main(){
    vector<int> vec1({1, 3});
    vector<int> vec2({2, 4});

    Solution sol;
    cout << setprecision(10) << sol.findMedianSortedArrays(vec1, vec2) << endl; // 2.5
    
    vector<int> vec3({100000});
    vector<int> vec4({100001});
    cout << sol.findMedianSortedArrays(vec3, vec4) << endl;
}
