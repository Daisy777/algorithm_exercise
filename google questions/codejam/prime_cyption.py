
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
    
def decryption(arr, n):
    message = [0] * (n+1)
    for i in range(n-1):
        if arr[i] != arr[i+1]:
            base = i+1
            message[base] = gcd(arr[i], arr[i+1])
    for i in range(base-1, -1, -1):
        message[i] = arr[i] // message[i+1]
    for i in range(base, n):
        message[i+1] = arr[i] // message[i]
    all_alphabet = list(set(message))
    all_alphabet.sort()
    alphabet_dict = {value: chr(index+ord('A')) for index, value in enumerate(all_alphabet)}

    return ''.join([alphabet_dict[number] for number in message])

if __name__ == '__main__':
    testnum = int(input().strip())
    for test in range(1, testnum+1):
        limit, length = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        print('Case #{}: {}'.format(test, decryption(arr, length)))

