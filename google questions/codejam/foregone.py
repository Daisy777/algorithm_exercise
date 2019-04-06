def foregone(n):
    i = 0
    result = 0
    while(n>0):
        if n % 10 == 4:
            result += 10**i
        i += 1
        n //= 10
    return result

if __name__ == '__main__':
    testnum = int(input())
    for test in range(testnum):
        n = int(input())
        result = foregone(n)
        print(''.join(['Case #', str(test+1), ': ', str(result), ' ',str(n-result)]))
    