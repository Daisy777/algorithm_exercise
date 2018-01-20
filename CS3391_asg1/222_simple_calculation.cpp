#include <cstdio>
#include <string>
#include <iostream>
#include<algorithm>
using namespace std;
#define SIZE 100

int main(){
	string inputLine;
	double inputNum;
	double sum=0; 
	while(getline(cin, inputLine)!=NULL){
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
					inputNum = atof(charNum);
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
					loc = 0;
					inputNum = atof(charNum);
					sum+= inputNum;
					// printf("%.4f", sum);
					memset(charNum, '\0',SIZE);
				}
			}
			

		}
		printf("%.4f\n",sum);
		sum = 0;
	}

	return 0;
	
}