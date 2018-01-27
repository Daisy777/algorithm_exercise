#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
int flag[100005];

void isPrime();
int largest_prime_substring(char* input);
int to_decimal(char* str);
int main(){
    char input[256];
    isPrime();
    while(scanf("%s", input)!= EOF){
        if(strtol(input, NULL, 10)==0)
            break;
        printf("%d\n", largest_prime_substring(input));
    }
    
    return 0;
}
void isPrime(){
    memset(flag, 0, 100005);
    flag[1] = 1;
    flag[0] = 1;
    for(int i=0; i<100000;i++){
        if(flag[i]==0){
            for(int j=i+i; j<100000;j+=i){
                flag[j] = 1;
            }
        }
    }
}

//don't forget to add a base conditioin
int largest_prime_substring(char* input){
    int len = 0;
    int maxnum = 0;
    while(input[len]!='\0'){len++;}
    int size = len>=5?5:len;
    char* outstr = new char[size+1]; //don't use size like      char outstr[size+1]!!!!!!

    if(size!=0){
        //spilt
        for(int i=0; i<=len-size;i++){
            for(int j=i; j<i+size; j++){
                outstr[j-i] = input[j];
            }
            outstr[size] = '\0';
            int temp_sub = strtol(outstr, NULL, 10);
            if(flag[temp_sub]==0 && temp_sub>maxnum){
                maxnum = temp_sub;
            }else{
                char* sub_out1 = new char[size];
                char* sub_out2 = new char[size];
                for(int i=0; i<size-1;i++){
                    sub_out1[i] = outstr[i];
                    sub_out2[i] = outstr[i+1];
                }
                sub_out1[size-1] = '\0';
                sub_out2[size-1] = '\0';
                int  maxi = max(largest_prime_substring(sub_out1),largest_prime_substring(sub_out2));
                maxnum = max(maxnum,maxi);
            }
        }
    }else{
        return 0;
    }
    
    return maxnum;
}

// int to_decimal(char* str){
//     int len=0;
//     int result = 0;
//     while(str[len]!='\0'){len++;}
//     for(int i=1; i<=len; i++){
//         result+=(str[i-1]-'1'+1)*pow(10, len-i);    //should change the char type to num before calculation
//     }
//     return result;
// }

// char* to_char(int num){
//     int len=0;
//     char* str=new char[1000];
//     memset(str, '\0', 1000);
//     int remainder = num;
//     while(remainder!=0){
//         str[len++] = remainder%10-1+'1';
//         remainder /= 10;
//     }
//     reverse(str, str+len);
//     str[len++] = '\0';
//     return str;
// }

//use strtol(), strtold() and so on
//don't try to write it by yourself anymore


