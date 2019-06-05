
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        length = len(board)
        if not length:
            return True 
            
        for i in range(length):
            rowset = set()
            colset = set()
            blockset = set()

            for j in range(length):
                if board[i][j] == '.' or board[i][j] not in rowset:
                    rowset.add(board[i][j])
                else:
                    return False 

                if board[j][i] == '.' or board[j][i] not in colset:
                    colset.add(board[j][i])
                else:
                    return False
                
                if board[j//3+(i//3)*3][j%3+(i%3)*3] == '.' or board[j//3+(i//3)*3][j%3+(i%3)*3] not in blockset:
                    blockset.add(board[j//3+(i//3)*3][j%3+(i%3)*3])
                else:
                    return False
        return True 


if __name__ == '__main__':
    test2 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    test1 = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
    ]
    print(Solution().isValidSudoku(test1))
    print(Solution().isValidSudoku(test2))
                
                