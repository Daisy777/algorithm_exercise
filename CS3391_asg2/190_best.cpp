/*****************************************
 * (This comment block is added by the Judge System)
 * Submission ID: 1736
 * Submitted at:  2013-01-22 21:41:07
 *
 * User ID:       40
 * Username:      52716792
 * Problem ID:    190
 * Problem Name:  Equation (UVa 727)
 */

#include <stdio.h>
#include <string.h>

bool cpmop(char a,char b){
	if(a=='('||a=='['||a=='{')
		return 1;
	if((b=='*'||b=='/')&&(a=='+'||a=='-'))
		return 1;
	return 0;
}
int main(){
	int all=0;
	scanf("%d",&all);
	all+=2;
	for(int t=0;t<all;t++){
	//while(1){
		char stack[50]={};
		int top=-1;
		
		char tempString[64]={};
		char eq[64]={};
		int index=0;
		
		while(gets(tempString)&&tempString[0]!=0){
			eq[index]=tempString[0];
			index++;
		}
		int length=strlen(eq);
		if(length==0){
			continue;
		}
		//gets(eq);
		for(int n=0;n<length;n++){
			if(eq[n]=='+'||eq[n]=='-'||eq[n]=='*'||eq[n]=='/'){
				while(top>=0){
					if(cpmop(stack[top],eq[n])){
						break;
					}else{
						printf("%c",stack[top]);
						top--;
					}
				}
				top++;
				stack[top]=eq[n];
			}else if(eq[n]=='('||eq[n]=='['||eq[n]=='{'){
				top++;
				stack[top]=eq[n];
			}else if(eq[n]==')'||eq[n]==']'||eq[n]=='}'){
				while(top>=0){
					if(stack[top]=='('||stack[top]=='['||stack[top]=='{'){
						top--;
						break;
					}else{
						printf("%c",stack[top]);
						top--;
					}
				}
			}else if(eq[n]>='0'&&eq[n]<='9'){
				printf("%c",eq[n]);
			}
		}
		while(top>=0){
			printf("%c",stack[top]);
			top--;
		}
        if(t!=all-1){
            printf("\n");
        }
		printf("\n");
	}
}