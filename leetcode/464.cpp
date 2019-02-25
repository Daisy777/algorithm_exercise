#include <vector>
#include <iostream>
using namespace std;

class Solution {
	enum RESULT { UNKNOWN, WIN, LOSE };
public:
	bool canIWin(int maxChoosableInteger, int desiredTotal) {
		if (maxChoosableInteger >= desiredTotal) return true;

		int s = maxChoosableInteger * (maxChoosableInteger + 1) / 2;
		if (s < desiredTotal) return false;
		if (s == desiredTotal) return maxChoosableInteger % 2;
	
		vector<RESULT> memo(1 << (maxChoosableInteger + 1), UNKNOWN);

		return dfs(maxChoosableInteger, desiredTotal, memo);
	}
private:
	bool dfs(int max, int t, vector<RESULT> &memo, int k = 0) {
		if (t <= 0) return false;
		if (memo[k] != UNKNOWN)	return memo[k] == WIN;

		for (int i = 1; i <= max; i++) {
			if (!(k & 1 << i) && !dfs(max, t - i, memo, k | (1 << i))) {
				memo[k] = WIN;
				return true;
			}
		}
		memo[k] = LOSE;
		return false;
	}
};

int main() {
    cout << Solution().canIWin(10, 11) << endl;
}