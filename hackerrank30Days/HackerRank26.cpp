/*
Author:    ZHAO Zinan
Created: 19-Oct-2018

nested logic
*/
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int expectedYear,expectedMonth, expectedDay;
    int returnYear, returnMonth, returnDay;

    cin >> returnDay >> returnMonth >> returnYear;
    cin >> expectedDay >> expectedMonth >> expectedYear;

    if (returnYear < expectedYear ||
        (returnYear == expectedYear && returnMonth < expectedMonth) ||
        (returnYear == expectedYear && returnMonth == expectedMonth && returnDay <= expectedDay)) {
        cout << 0 << endl;
    } else if (returnYear == expectedYear && returnMonth == expectedMonth) {
        cout << 15*(returnDay - expectedDay) << endl;
    } else if (returnYear == expectedYear) {
        cout << 500*(returnMonth - expectedMonth) << endl;
    } else {
        cout << 10000 << endl;
    }

    return 0;
}
