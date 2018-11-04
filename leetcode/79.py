'''
Author:    ZHAO Zinan
Created: 04-Nov-2018


'''
class Solution:
    def init(self, board):
        self.letterlist = {}
        for row, rowval in enumerate(board):
            for col, colval in enumerate(rowval):
                if colval not in self.letterlist:
                    self.letterlist[colval] = [(row, col)]
                else:
                    self.letterlist[colval].append((row, col))
                    
    def _exist(self, board, string, beginCoor):
        if len(string) == 0:
            return True
        
        x = beginCoor[0] 
        y = beginCoor[1]
        init_value = board[x][y]

        board[x][y] = None
        
        larger_x = min(len(board)-1, x+1)
        larger_y = min(len(board[0])-1, y+1)
        smaller_x = max(0, x-1)
        smaller_y = max(0, y-1)
        
        result = False
        for i in [larger_x, smaller_x]:
            if board[i][y] == string[0]:
                result = result or self._exist(board, string[1:], (i, y))
            
        for j in [larger_y, smaller_y]:
            if board[x][j] == string[0]:
                result = result or self._exist(board, string[1:], (x, j))
        board[x][y] = init_value
        return result
                    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not len(word):
            return True
        if not len(board) or not len(board[0]):
            return False
        
        # find the first begin coordinate in board
        self.init(board)
        if word[0] not in self.letterlist.keys():
            return False
        first_coor = self.letterlist[word[0]]
        result = False
        for pair in first_coor:
            result = result or self._exist(board, word[1:], pair)
        return result
        
    
# test
if __name__ == '__main__':
    # board =[
    #     ['A','B','C','E'],
    #     ['S','F','C','S'],
    #     ['A','D','E','E']
    # ]
    solution = Solution()
    # print(solution.exist(board, 'SEE')) # true
    # print(solution.exist(board, 'ABCCED')) # true
    # print(solution.exist(board, 'ABCB')) # false

    # board1 = [['a']]
    # print(solution.exist(board1, 'b')) # false

    board2 = [
        ['C', 'A', 'A'],
        ['A', 'A', 'A'],
        ['B', 'C', 'D']
    ]
    print(solution.exist(board2, 'AAB')) # true