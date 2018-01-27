#include<cstdio>
#include<cstring>
#include<algorithm>
#define WORD 105
using namespace std;

//one number -> len is one
//i to record the **location** and len to record the length
//don't use the same variable !!!!(endless loop for word with numbers)
int len(char word[]){
	int len=0; 
	while(word[len]!='\0'){len++;}
	return len;
}

void smallLetters(char word[]){
	int len=0;
	while(word[len]!='\0'){len++;}
	for(int i=0; i<len; i++){
		if(word[i]<='Z' && word[i]>='A'){
			word[i] = word[i]-'A'+'a';
		}
	}
}

void clearFormat(char word[]){
	int length = len(word);
	// printf("%d\n", length);
	char cleard[WORD];
	int loc = 0;
	for(int i=0; i<length; i++){
		if((word[i]<='z' && word[i]>='a')||(word[i]<='Z'&& word[i]>='A')||(word[i]=='-')){
			cleard[loc++] = word[i];
		}
	} 
	cleard[loc] = '\0';
	strcpy(word, cleard);
}

int main(){
	char input[WORD];
	char word[WORD];
	int maxlen = 0;
	while(scanf("%s", input) && strcmp(input, "E-N-D")!=0){
		clearFormat(input);
		int length = len(input);
		// printf("length=%d\n", length);
		if(maxlen ==0 || maxlen < length){
			maxlen = length;
			strcpy(word, input);
		}
		memset(input, '\0', WORD);
	}
	smallLetters(word);
	printf("%s\n", word);
	return 0;
}