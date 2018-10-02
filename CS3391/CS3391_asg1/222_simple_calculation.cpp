#include <cstdio>
#include <cstring>
#include<string>
#include <iostream>
#include <algorithm>
#include<cstdlib>
using namespace std;
#define SIZE 100

int main(){
	string inputLine;
	long double inputNum;
	long double sum=0; 
	int count = 0;
	while(getline(cin, inputLine)!=NULL){
		if(count!=0){
			printf("\n");
		}
		count++;
		bool begin = false;
		char charNum[SIZE];
		memset(charNum, '\0', SIZE);
		int loc = 0;
		for(int i=0; i<inputLine.size(); i++){
			if(i!=inputLine.size()-1){
				if(begin==false && inputLine[i]!=' '){
					begin = true;
					charNum[loc++] = inputLine[i];
				}else if(begin==true && inputLine[i]==' ' ){
					begin = false;
					charNum[loc++] = '\0';
					// printf("charNum = %s\n", charNum);
					inputNum = strtold(charNum, NULL);
					// printf("%.10Lf\n", inputNum);
					sum+= inputNum;
					// printf("sum = %.4f\n", sum);
					memset(charNum, '\0', SIZE);
					loc  = 0;
				}else if(begin==true && inputLine[i]!=' '){
					charNum[loc++] = inputLine[i];
				}
			}else{
				if(inputLine[i]!=' '){
					charNum[loc++] = inputLine[i];
					begin = false;
					charNum[loc++] = '\0';
					inputNum = strtold(charNum, NULL);
					// printf("%.10Lf\n", inputNum);
					loc = 0;
					sum+= inputNum;
					// printf("%.4f", sum);
					memset(charNum, '\0',SIZE);
				}
			}
			

		}
		printf("%.4Lf\n",sum);
		sum = 0;
	}

	return 0;
}
