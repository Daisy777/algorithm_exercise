import sys

# number of test cases
n = int(input())

# read test case one by one 
i = 0

for line in sys.stdin:
    # use rstrip to remove the extra space of the input
    line = line.rstrip()
    print('{} {}'.format(line[::2], line[1::2]))

    i += 1
    if i >= n:
        break
    
