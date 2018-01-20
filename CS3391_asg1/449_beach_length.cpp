#include<cstdio>
#include<string>
#include<algorithm>
using namespace std;
#define ELE 55
#define KINDOM 55

int sumInRow(char elemetn[], int col);
int sumBetweenCol(char last[], char ele[], int col);
//what's the meaning of "Input ends with EOF???? the end of file or a EOF string????"
int main(){
	char lastEle[ELE];
	char element[ELE];
	memset(lastEle, '\0', ELE);
	memset(element, '\0', ELE);
	int col=0; 
	int sum = 0;
	while(scanf("%s", element)!=EOF){
		printf("element= %s\n", element);
		if(!col){
			while(element[col]!='\0'){col++;}
		}
		if(lastEle[0]!='\0'){
			sum+=sumBetweenCol(lastEle, element, col);
		}
		sum+=sumInRow(element, col);
		strcpy(lastEle, element);
	}
	printf("%d\n", sum);
	sum = 0;
	col = 0;
	memset(lastEle, '\0', ELE);
	memset(element, '\0', ELE);

}

int sumInRow(char ele[], int col){
	int begin = 0;
	bool counting = false;
	int sum=0;

	if(ele[0]=='#')
		begin = -1;
	for(int i=0; i<col; i++){
		if(counting==false && ele[i]=='#'){
			sum++;
			counting = true;
		}else if(counting==true && ele[i]=='.'){
			sum++;
			counting = false;
		}
	}
	// printf("sum = %d\nbegin=%d\n", sum, begin);

	return sum+begin;
}

int sumBetweenCol(char last[], char ele[], int col){
	int sum=0;
	for(int i=0; i<col; i++){
		if(ele[i]=='#'){
			if(last[i]!='#')
				sum++;
			if(i!=col-1 && last[i+1]!='#'){
				sum++;
			}
		}
		if(last[i]=='#'){
			if(ele[i]!='#')
				sum++;
			if(i!=0 && ele[i-1]!='#'){
				sum++;
			}
		}
	}
	return sum;
}
