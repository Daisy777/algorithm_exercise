#include<cstdio>
#include<algorithm>
using namespace std;

int flag[100000];
void prime(){
	memset(flag, 0, 100000);
	flag[0] = 1;
	flag[1] = 1;
	for(int i=2; i<100000; i++){
		if(flag[i]==0){
			for(int j=2*i; j<100000; j+=i){
				flag[j] = 1;
			}
		}
	}
} 




int main(){
	prime();
	int num; 
	while(scanf("%d", &num) && num!=0){
		if(flag[num]==0){
			printf("%s\n", "prime");
		}else{
			printf("%s\n", "not prime");
		}
	}

	return 0;
}