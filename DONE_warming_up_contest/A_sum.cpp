#include <cstdio>
using namespace std;

int main(){
	int a=0, b=0;
	while(scanf("%d %d", &a, &b) != EOF){
		int sum = a+b;
		printf("%d\n", sum);
	}
	return 0;
}