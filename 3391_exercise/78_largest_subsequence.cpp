#include<cstdio>
#include<algorithm>
#include<string>
#include<unordered_map>
#define LEN 55
using namespace std;

int main(){
	int size;
	char sub[LEN];
	char str[LEN];

	scanf("%d", &size);
	for(int i=0; i<size; i++){
		int len = 0;
		int len_sub =0;
		memset(str, '\0', LEN);
		memset(sub, '\0', LEN);

		scanf("%s", str);
		while(str[len]!='\0'){len++;}
		char max_char = 'a';
		int max_index=-1;
		bool bre = false;
		
		while(bre==false){
			bre = true;
			int beginP = max_index+1;
			max_char = 'a'-1;
			for(int i=beginP;i<len; i++){				
				if(str[i]==str[beginP-1]){                        
					max_char=str[i];
					bre = false;
					max_index=i;
					break;
				}else if(str[i]>max_char){
					max_char=str[i];
					bre = false;
					max_index=i;
				}
				// printf("%c", max_char);
			}
			if(bre ==false){
				sub[len_sub++] = max_char;
				// printf("%c", sub[len_sub-1]);
				// printf("%d", len_sub);	
			}

		}
		for(int i=0; i<len_sub;i++){
			printf("%c", sub[i]);
		}
		printf("\n");
	}
	return 0;
}


//test   use the first t in the first loop
//testtt use the second t in the second loop  -> not the last one!!!

