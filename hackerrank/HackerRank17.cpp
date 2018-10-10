/*
Author:    ZHAO Zinan
Created: 10-Oct-2018

practice throwing and propagating exception
*/
#include <cmath>
#include <iostream>
#include <exception>
#include <stdexcept>
using namespace std;

//Write your code here
class Calculator {
public:
    int power(int a, int b) {
        if (a < 0 || b < 0) {
            throw invalid_argument("n and p should be non-negative");
        }
        
        if (b == 0) {
            return 1;
        }

        int mid = power(a, b/2);
        if (b%2 == 0) {
            return mid*mid;
        } else {
            return mid*mid*a;
        }
    }


};

int main()
{
    Calculator myCalculator=Calculator();
    int T,n,p;
    cin>>T;
    while(T-->0){
      if(scanf("%d %d",&n,&p)==2){
         try{
               int ans=myCalculator.power(n,p);
               cout<<ans<<endl; 
         }
         catch(exception& e){
             cout<<e.what()<<endl;
         }
      }
    }
    
}