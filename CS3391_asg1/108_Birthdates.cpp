#include<cstdio>
#include<string>
#include<algorithm>
using namespace std;
#define strSize 16

class Person{
private:
	char name[strSize];
	int day, month, year;
public:
	Person(){
		day=0; 
		month =0; 
		year=0;}
	Person(char n[], int d , int m, int y){
		strcpy(name, n);
		day = d;
		month = m;
		year = y;
	}
	char* getName(){
		return name;
	}
	friend int compare(Person x, Person y){
		if(x.year>y.year){
			return -1; 
		}else if(x.year<y.year){
			return 1;
		}else{
			if(x.month>y.month){
				return -1;
			}else if(x.month<y.month){
				return 1;
			}else{
				if(x.day>y.day){
					return -1;
				}else if(x.day<y.day){
					return 1;
				}else{
					return 0;
				}
			}
		}
	}

};

int main(){
	int num;
	char name[strSize];
	int day, month, year;
	Person youngest, oldest;

	scanf("%d", &num);
	for(int i=0; i<num; i++){
		scanf("%s %d %d %d", name, &day, &month, &year);
		// printf("nameinput: %s", name);
		Person temp_person = Person(name, day, month, year);
		// printf("%s\n", temp_person.getName());
		if(i==0){
			youngest  =temp_person;
			oldest = temp_person;
		}else{
			if(compare(temp_person, youngest)==-1){
				youngest = temp_person;
			}
			if(compare(temp_person, oldest)==1){
				oldest = temp_person;
			}
		}
		memset(name, '\0', strSize);
		// printf("%s\n", name);
	}
	printf("%s\n", youngest.getName());
	printf("%s\n", oldest.getName());
}
