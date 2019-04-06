testnum = int(input())
for t in range(1, testnum+1):
    length = int(input())
    paths = input()
    choice = {'S':'E', 'E':'S'}
    result = [choice[i] for i in paths]
    print ('Case #%s: %s' % (t, ''.join(result)))