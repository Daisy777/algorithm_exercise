def paint(walls):
    if len(walls) == 0:
        return 0
    blocks = list(map(int, walls))
    length = len(walls)
    num_walls = (length+1)//2

    # find subarray with max sum
    max_sum = max([sum(blocks[i:i+num_walls]) for i in range(length-num_walls+1)])
    return max_sum

numTest = int(input().strip())
for i in range(numTest):
    walls = input().strip()
    print(''.join(['Case #', str(i+1), ': ', str(paint(walls))]))