# watermelon
# if the boys can divide the watermelon into two parts, each of them weighing even number of kilos
# weight should be possitive
weight = int(input().strip())
result = 'YES' if weight%2 == 0 and weight >2 else 'NO'
print(result)