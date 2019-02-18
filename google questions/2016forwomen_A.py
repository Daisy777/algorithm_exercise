def sales_price(prices):
    sales_n_origin = {}
    result = []
    for price in prices:
        if price*0.75 in sales_n_origin and sales_n_origin[price*0.75]:
            result.append(int(price*0.75))
            sales_n_origin[price*0.75] -= 1
        elif price in sales_n_origin:
            sales_n_origin[price] += 1
        else:
            sales_n_origin[price] = 1
    return ' '.join(map(str, result))
        

if __name__ == '__main__':
    output = open('output', 'a')
    with open('A-small-practice.in', 'r') as f:
        numtest = int(f.readline().strip())
        for test in range(numtest):
            lentest = int(f.readline().strip())
            prices = list(map(int, f.readline().strip().split()))
            output.write(''.join(['Case #', str(test+1), ': ', sales_price(prices), '\n']))
