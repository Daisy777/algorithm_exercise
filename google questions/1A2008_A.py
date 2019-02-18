def MinimumScalarProduct(nums1, nums2):
    return sum([i*j for i, j in zip(sorted(nums1), sorted(nums2, reverse=True))])

if __name__ == '__main__':
    with open('A-small-practice.in', 'r') as infile:
        numtest = int(infile.readline().rstrip())
        for test in range(numtest):
            lentest = int(infile.readline().rstrip())
            nums1 = list(map(int, infile.readline().rstrip().split()))
            nums2 = list(map(int, infile.readline().rstrip().split()))
            with open('1A2008_a_small_practice.out', 'a') as f:
                f.write(''.join(['Case #', str(test+1), ': ', str(MinimumScalarProduct(nums1, nums2)), '\n']))