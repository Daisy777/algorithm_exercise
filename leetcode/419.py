class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if len(board) == 0 or len(board[0]) == 0:
            return 0

        rowlen = len(board)
        collen = len(board[0])
        warnum = 0
        for rownum in range(len(board)):
            row = board[rownum]

            for colnum in range(len(row)):
                ele = row[colnum]
                if ele == 'X':
                    row[colnum] = '.'
                    warnum += 1

                    # after finding one war, change all the X in same col/row to
                    # no war state
                    tempcolnum = colnum
                    while (tempcolnum+1 < collen and row[tempcolnum+1]=='X'):
                        row[tempcolnum+1] = '.'
                        tempcolnum += 1
                    temprownum = rownum
                    while (temprownum+1 < rowlen and board[temprownum+1][colnum]=='X'):
                        board[temprownum+1][colnum] = '.'
                        temprownum += 1
        
        return warnum

# test
if __name__ == '__main__':
    board = [
        ['X', '.', '.', 'X'],
        ['.', '.' ,'.', 'X'],
        ['.', '.', '.', 'X']
    ]

    print(Solution().countBattleships(board)) # 2


    board = [
        ["X",".","X"],
        ["X",".","X"]
    ]

    print(Solution().countBattleships(board)) # 2
                