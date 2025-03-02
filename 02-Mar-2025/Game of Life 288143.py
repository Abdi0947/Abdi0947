# Problem: Game of Life - https://leetcode.com/problems/game-of-life/description/

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None. Modifies board in-place.
        """
        if not board or not board[0]:  
            return

        rows, cols = len(board), len(board[0])
        original = [[board[r][c] for c in range(cols)] for r in range(rows)]  

        for r in range(rows):
            for c in range(cols):
                live_neighbors = 0  
                for nr in range(r-1, r+2):
                    for nc in range(c-1, c+2):
                        if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) != (r, c):
                            if original[nr][nc] == 1:
                                live_neighbors += 1  
                if original[r][c] == 1:  
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = 0  
                else:  
                    if live_neighbors == 3:
                        board[r][c] = 1  

sol = Solution()
board = [[0, 1, 0], 
         [0, 0, 1], 
         [1, 1, 1], 
         [0, 0, 0]]
sol.gameOfLife(board)
print(board)
