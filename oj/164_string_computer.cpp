#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define SIZE 20

char* longest_str(char* str1, char *str2);
int main(){
	char fromStr[SIZE];
	char toStr[SIZE];
	while(scanf("%s", fromStr)!=EOF && fromStr[0]!='#'){
		scanf("%s", toStr);




		memset(fromStr, '\0',SIZE);
		memset(toStr, '\0',SIZE);
	}

	return 0;
}

char* longest_str(char* str1, char *str2){
	int len1 =0, len2=0;
	while(str1[len1]!='\0'){len1++;}
	while(str2[len2]!='\0'){len2++;}

	char* newStr1=NULL;
	char* newStr2 = NULL;
	strncpy(newStr1, str1+1, len1-1);
	strncpy(newStr2, str2+1, len2-1);

	
}

//O(n^2) ...
