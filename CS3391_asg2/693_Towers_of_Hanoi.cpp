#include<cstdio>
using namespace std;

//hanoiStep/2 = consecutive steps
int hanoiStep(int n){
	if(n==1){
		return 2;
	}else{
		return 6*(hanoiStep(n-1)/2)+2;
	}
}
int main(){
	int size;
	while(scanf("%d", &size)!=EOF){
		printf("%d\n", hanoiStep(size));
	}

	return 0;
}