#include <iostream>
#include <string>
#include <numeric>
#define max(a, b) ((a>b)?(a):(b))
using namespace std;

int mural(string wall, int length) {
    int numBlocks = (length+1)/2;
    int* wallArr = new int[sizeof(wall)];

    for(int i=0; i<length; i++) {
        wallArr[i] = wall[i]-'0';
    }

    int maxSum = 0;

    for(int i=0; i<length-numBlocks+1; i++) {
        int temp = accumulate(wallArr+i, wallArr+i+numBlocks, 0);
        maxSum = max(maxSum, temp);
    }
    return maxSum;
}
int main() {
    int numTest;
    cin >> numTest;
    for(int i=0; i<numTest; i++) {
        int length;
        string wall;
        cin >> length >> wall;
        cout << "Case #" << i+1 << ": " << mural(wall, length) << endl;
    }

    return 0;
}