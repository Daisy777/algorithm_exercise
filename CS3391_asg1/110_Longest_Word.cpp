#include<cstdio>
#include<cstring>
#include<algorithm>
#define WORD 105
using namespace std;


int len(char word[]){
	int len=0; 
	while(word[len]!='\0' && word[len]!='.' && word[len]!=','){len++;}

	return len;
}

int main(){
	char inputWord[WORD];
	char word[WORD];
	int maxlen = 0;
	while(scanf("%s", inputWord) && strcmp(inputWord, "E-N-D")!=0){
		int length = len(inputWord);
		if(maxlen ==0 || maxlen < length){
			maxlen = length;
			strcpy(word, inputWord);
		}
		memset(inputWord, '\0', length);
	}
	printf("%s\n", word);
	return 0;
}