'''
Author: ZHAO Zinan
Created: 30. April 2019


''' 
from typing import List, Tuple, Dict, TextIO
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        # record location of X and O 
        locx, loco = set(), set()
        for i, row in enumerate(board):
            for j, ele in enumerate(row):
                if board[i][j] == 'X':
                    locx.add((i, j))
                elif board[i][j] == 'O':
                    loco.add((i, j))
            
        # order
        if not (len(locx) == len(loco) + 1 or len(locx) == len(loco)):
            return False 
        
        # continue after complete
        winnum, win = 0, []
        for i in range(3):
            # check row
            if len(set(board[i])) == 1 and board[i][0] != ' ':
                winnum += 1
                win.append(board[i][0])
            
            # check col
            col = [row[i] for row in board]
            if len(set(col))== 1 and col[0] != ' ':
                winnum += 1
                win.append(col[0])

        # check diagonal
        if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != ' ':
            winnum += 1
            win.append(board[0][0])
        if board[0][2] == board[1][1] and board[2][0] == board[1][1] and board[0][2] != ' ':
            winnum += 1
            win.append(board[0][2])
            
        print(win)
        if winnum > 2:
            return False 
        if winnum == 1:
            if win[0] == 'X':
                return len(locx) == len(loco) + 1
            else:
                return len(locx) == len(loco)
        if winnum == 2:
            return win[0] == 'X' and win[1] == 'X' and len(locx) == len(loco) + 1
        return True

if __name__ == '__main__':
    print(Solution().validTicTacToe(["O  ", "   ", "   "]))
    print(Solution().validTicTacToe(["XOX", " X ", "   "]))
    print(Solution().validTicTacToe(["XXX", "   ", "OOO"]))
    print(Solution().validTicTacToe(["XOX", "O O", "XOX"]))
    print(Solution().validTicTacToe(["XXX","OOX","OOX"])) # 🌟 
    print(Solution().validTicTacToe(["XXO","XOX","OXO"])) # 🌟 