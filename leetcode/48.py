class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # zip -> not inplace
        n = len(matrix)
        # transpose
        if not n:
            return matrix
        
        for i in range(n):
            for j in range(i, n): # if j in range(n) transpose two times means it will become the origin matrix...
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
               
       
        # reverse each row
        for index, row in enumerate(matrix):
            for j in range(n//2):
                matrix[index][j], matrix[index][len(row)-1-j] = matrix[index][len(row)-1-j], matrix[index][j]
                

# test
if __name__ == '__main__':
    matrix0 = [
        [1, 2, 3], 
        [4, 5, 6],
        [7, 8, 9]
    ]
    Solution().rotate(matrix0)
    print(matrix0)