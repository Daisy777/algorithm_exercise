def hero_to_zeroa(n:int, k:int)->int:
    step = 0
    while(n>0):
        step += n%k
        n = (n//k) * k
        
        if n == 0:
            break
        step += 1
        n //= k 
    return step 

numtest = int(input().strip())
for _ in range(numtest):
    line = input().strip().split() 
    print(hero_to_zeroa(int(line[0]), int(line[1])))
