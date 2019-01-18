'''
Author: ZHAO Zinan
Created: 07-Oct-2018
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class Difference {
    private:
    vector<int> elements;
  
    public:
    int maximumDifference;
    Difference(vector<int> eles) {
        elements = eles;
    }

    void computeDifference() {
        int maxdiff = 0;
        for (vector<int>::iterator i = elements.begin(); i != elements.end(); i++) {
            for (vector<int>::iterator j = i+1; j != elements.end(); j++) {
                int diff = abs(*j - *i);
                maxdiff = max(maxdiff, diff);
            }
        }
        maximumDifference = maxdiff;
    }

}; // End of Difference class

int main() {
    int N;
    cin >> N;
    
    vector<int> a;
    
    for (int i = 0; i < N; i++) {
        int e;
        cin >> e;
        
        a.push_back(e);
    }
    
    Difference d(a);
    
    d.computeDifference();
    
    cout << d.maximumDifference;
    
    return 0;
}