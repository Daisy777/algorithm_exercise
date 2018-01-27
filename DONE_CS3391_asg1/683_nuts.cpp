#include<cstdio>
#include<cmath>
#include<algorithm>
#include<cstring>
#define SIZE 1000
using namespace std;

int main(){
	int maxNumBox, nut, divisor, capacity;
	while(scanf("%d %d %d %d", &maxNumBox, &nut, &divisor, &capacity)!=EOF){
		int* numOfDiv = new int[SIZE];
		int numWithSec = 0;
		int reminder = divisor;
		memset(numOfDiv, 0, SIZE);
		while(reminder!=0){
			if(reminder>maxNumBox-1){
				numOfDiv[numWithSec++] = maxNumBox-1;
				reminder-=maxNumBox-1;
			}else{
				if(reminder>0){
					numOfDiv[numWithSec++] = reminder;
					reminder = 0;
				}
			}
		}
		// test the number of divisors in each box
		// for(int i=0; i<numWithSec;i++){
		// 	printf("%d ", numOfDiv[i]);
		// }
		// printf("\n");

		int numOfBox = 0;
		int reminderOfNut = nut;
		while(reminderOfNut!=0){
			if(reminderOfNut>(numOfDiv[numOfBox]+1)*capacity){
				reminderOfNut-=(numOfDiv[numOfBox]+1)*capacity;
			}else{
				reminderOfNut=0;
			}
			numOfBox++;
		}

		printf("%d\n", numOfBox);

	}
	return 0;
}
