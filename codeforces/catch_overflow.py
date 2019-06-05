def addcheck(k:int, times:int) -> int:
    if k <= 2**32 -1-times:
        return k+times 
    else:
        return False 

stack = []
numoperation = int(input().strip())
for _ in range(numoperation):
    operation = input().strip() 
    