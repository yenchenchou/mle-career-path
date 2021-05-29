#51. N-Queens
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # keep track of col, diagonal, antidiagonal
        # use back track
        
        def create_board(state):
            return ["".join(row) for row in state]
        
        def backtrack(row, cols, diagonals, antidiagonals, cur_state):
            if row == n:
                ans.append(create_board(cur_state))
                return 
            
            for col in range(n):
                cur_diagonal = row - col
                cur_antidiagonal = row + col
                if col in cols or cur_diagonal in diagonals or cur_antidiagonal in antidiagonals:
                    continue
                
                cols.add(col)
                diagonals.add(cur_diagonal)
                antidiagonals.add(cur_antidiagonal)
                state[row][col] = "Q"
                
                backtrack(row+1, cols, diagonals, antidiagonals, state)
                cols.remove(col)
                diagonals.remove(cur_diagonal)
                antidiagonals.remove(cur_antidiagonal)
                state[row][col] = "."
                
                
        ans = []
        state = [["."]*n for i in range(n)]
        backtrack(0, set(), set(), set(), state)
        return ans  #O(N!) -> the factorial of n, O(n^2) -> 3n(sets) + n(stack) + n(state cost)
        