# use dynamic programming to solve 0-1 knapsack problem
# fault when writing the code:
#  index + 1 as len(col) = len(items)+1
#  define item class as it has bath val and weight

class Item:
    def __init__(self, val, weight):
        self.val = val
        self.weight = weight

def knapsack(items: list, limit: int) -> int:
    dp = [[0 for i in range(len(items)+1)]  for j in range(limit+1)]
    for i in range(1, limit+1):
        for index, item in enumerate(items):
            if item.weight <= limit:  
                dp[i][index+1] = max(dp[i][index], dp[i-item.weight][index]+item.val)
            else:
                dp[i][index+1] = dp[i][index]

    print(dp)
    return dp[limit][len(items)]

# test 
if __name__ == '__main__':
    print(knapsack([], 10)) # 0
    print(knapsack([Item(10, 10)], 10)) # 10
    print(knapsack([Item(2, 10)], 0)) # 0