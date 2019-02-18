def evenDigits(num):
    even = [0, 2, 4, 6, 8]
    highest = len(str(num))
    loc = highest
    remaining = num
    highest_odd = 0

    while(loc>1):
        if remaining//(10**(loc-1)) not in even:
            break
        else:
            remaining %= 10**(loc-1)
            loc = len(str(remaining))
    
    if loc == 1 and remaining in even:
        return 0
    
    smaller_one = (remaining//(10**loc)-1)**(10**loc) + (10**loc-1)//9*8
    if remaining//(10**loc) != 9:
        larger_one = (remaining//(10**loc)+1)**(10**loc)
    else:
        larger_one = 2*(10**(loc+1))
    print(larger_one, smaller_one)
    return min(larger_one-num, num-smaller_one)

if __name__ == '__main__':
    with open('test', 'r') as f:
        numtest = int(f.readline().strip())

        for i in range(numtest):
            cal = evenDigits(int(f.readline().strip()))
            with open('output', 'a') as output:
                output.write(''.join(['Case #', str(i+1), ': ', str(cal), '\n']))
                