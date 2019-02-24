# awsl
def _wakeup(allcombinations, i):
    sum = 0
    
    for combination in allcombinations:
        for index, ele in enumerate(combination):
            sum += ele*(index+1)**i
    return sum
        
                
def wakeup(A, K):
    sum = 0
    
    # calculate all combinations
    alladjcent = []
    def adjcent(arr, k):
        for i in range(len(arr)-k+1):
            yield arr[i:i+k]

    for i in range(1, len(A)+1):
        alladjcent.extend(list(adjcent(A, i)))
        
    for i in range(1, K+1):
        sum += _wakeup(alladjcent, i)
    return sum


# input
numTest = int(input().strip())
for i in range(numTest):
    N, K, x, y, C, D, E1, E2, F = map(int, input().strip().split())
    # generate array A
    if N == 0:
        print(0)
        continue
    
    A = [0]*N
    for _ in range(N):
        A[_] = (x+y)%F
        x, y = (C*x+D*y+E1)%F, (D*x+C*y+E2)%F
    print(''.join(['Case #', str(i+1), ': ', str(wakeup(A, K)%1000000007)]))
    