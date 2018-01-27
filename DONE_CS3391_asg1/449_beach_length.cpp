#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;
#define ELE 55

int sumInRow(char elemetn[], int col);
int sumBetweenRow(char last[], char ele[], int col, int count);

int main(){
	char islands[ELE][ELE];
	int sum = 0;
	char c= '\0';
	int bre = 0;
	int row = 0;
	int col=1;
	int len=0;

	//the first char of a test case
	while(scanf("%c", &c)!=EOF && bre != 1){
		islands[0][0]  = c;
		bre = 0;
		col = 0;
		row=0;
		sum=0;

		while(islands[row][0]!='\n'){ //if not, continues to the next test case
			//input the line
			while(islands[row][col]!='\n'){
				col++;
				if(scanf("%c", &islands[row][col])==EOF){
					bre = 1;
					break;
				}
			}
			row++;
			len = col;
			col=0;
			if(scanf("%c", &islands[row][0])==EOF){
				bre = 1;
				break;
			}	
		}
		for(int i=0; i<row-1; i++){
			sum+=sumInRow(islands[i], len);
			sum+=sumBetweenRow(islands[i], islands[i+1], len, i+2);
		}
		sum+=sumInRow(islands[row-1], len);

		//print the islands for test
		// for(int i=0; i<row; i++){
		// 	for(int j=0; j<len; j++){
		// 		printf("%c ", islands[i][j]);
		// 	}
		// 	printf("\n");
		// }
		// printf("\n");
		printf("%d\n", sum);
	}
	
	return 0;
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
	// printf("sumInRow = %d\n", sum+begin);

	return sum+begin;
}

int sumBetweenRow(char last[], char ele[], int col, int count){
	// printf("last=%s", last);
	// printf("ele=%s", ele);
	// printf("%d\n", col);
	// printf("count=%d\n", count);
	int sum=0;
	if(count%2==0){
		for(int i=0; i<col; i++){
			if(last[i]!=ele[i])
				sum++;
		}
		// printf("part1 = %d\n", sum);
		for(int i=0; i<col-1;i++){
			if(ele[i]!=last[i+1])
				sum++;
		}
	}else{
		for(int i=0; i<col; i++){
			if(ele[i]!=last[i])
				sum++;
		}
		// printf("part2 = %d\n", sum);
		for(int i=0; i<col-1;i++){
			if(last[i]!=ele[i+1])
				sum++;
		}	
	}
	
	// printf("sumBetweenCol=%d\n", sum);
	return sum;
}
