#include<cstdio>
#include<stack>
#include<vector>

using namespace std;
int compareP(char x, char y){
	if((x=='/' ||x=='*')&& (y=='/'||y=='*')){
		return 0;
	}else if((x=='/' || x=='*') && (y=='+'||y=='-')){
		return 1;
	}else if((x=='+'||x=='-') && (y=='/' || y=='*')){
		return -1;
	}else if((x=='+'||x=='-') && (y=='+'||y=='-')){
		return 0;
	}
	return -2;//error
}

//stack store two variables
//

int main(){
	int n;
	char c;
	scanf("%d", &n);
	stack<char> operators;
	vector<char> statement;
	int count=0;
	while(count<n){
		//before pop, check whether it is empty
		bool valid = true;
		while(scanf("%c", &c)!=EOF && c!='\n'){
			if(c<='9' && c>='0'){
				statement.push_back(c);
			}else if(c=='+' || c=='-' || c=='/' || c=='*'){
				if(operators.empty()){
					operators.push(c);
				}else{
					int compare = compareP(operators.top(), c);
					while(compare == 1 || compare==0){
						char temp = operators.top();
						operators.pop();
						statement.push_back(temp);
						if(operators.empty()){
							break;
						}else{
							compare = compareP(operators.top(), c);
						}
					}
					operators.push(c); //compare == -1
				}
				
			}else if(c=='('){
				operators.push(c);
			}else if(c==')'){
				while(operators.top()!='('){
					char temp = operators.top();
					operators.pop();
					statement.push_back(temp);
				}
				operators.pop();
			}
			scanf("%c", &c); //remove the \n in the end of each line
		}
		while(!operators.empty()){
			char temp = operators.top();
			operators.pop();
			statement.push_back(temp);
		}
		if(statement.empty()){
			valid = false;
		}
		if(valid){
			for(vector<char>::iterator v=statement.begin(); v!=statement.end(); v++){
				printf("%c", *v);
			}
			printf("\n");
			count++; //extra \n shouldn't be counted
			if(count!=n){
			printf("\n");
		}
		}
		//clear the stack and vector after each loop
		statement.clear();
	}
}