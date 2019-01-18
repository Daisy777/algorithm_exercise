# number of names
length = int(input())

# get the names and phone number
phoneBook = {}
for i in range(length):
    inputPair = input().split()
    phoneBook[inputPair[0]] = inputPair[1]

while True:
    try:
        name = input()
        if name in phoneBook.keys():
            print('{}={}'.format(name, phoneBook[name]))
        else:
            print('Not found')
    except:
        break