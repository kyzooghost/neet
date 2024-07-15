
// Capture surrounded regions
// Region - 'O' cell
// If region cell on edge of board - Cannot be surrounded
// DFS - if can reach out-of-bounds -> T, cannot -> F
// Lol purposely doing Leetcode when my brain is fried, and in C#
// Ok got in 35 minutes, 36% runtime and 48% memory
// Eih didn't do well on this question, this is a pretty standard graph medium
namespace SurroundedRegions
{
    // Much better, no need for new 'visited' array
    // 60% runtime, 79% memory
    public class Solution_V2 {
        public void Solve(char[][] board) {
            int rows = board.Length;
            int cols = board[0].Length;

            void dfs(int i, int j)
            {
                if (i < 0 || j < 0 || i >= rows || j >= cols) return;
                if (board[i][j] == 'X' || board[i][j] == 'T') return;
                board[i][j] = 'T';
                dfs(i+1, j);
                dfs(i-1, j);
                dfs(i, j+1);
                dfs(i, j-1);
            }

            // First pass to populate visited
            for (int r = 0; r < rows; r ++)
            {
                for (int c = 0; c < cols; c ++)
                {
                    if (r == 0 || c == 0 || r == rows - 1 || c == cols - 1) dfs(r, c);
                }
            }

            // Second pass to find non-visited 'O's
            for (int r = 0; r < rows; r ++)
            {
                for (int c = 0; c < cols; c ++)
                {
                    if (board[r][c] == 'O') board[r][c] = 'X';
                    else if (board[r][c] == 'T') board[r][c] = 'O';
                }
            }
        }
    }

    public class Solution {
        public void Solve(char[][] board) {
            int rows = board.Length;
            int cols = board[0].Length;
            var visited = new bool[rows][];

            for (int r = 0; r < rows; r ++)
            {
                visited[r] = new bool[cols];
                for (int c = 0; c < cols; c ++)
                {
                    visited[r][c] = false;
                }
            }

            void dfs(int i, int j)
            {
                if (i < 0 || j < 0 || i >= rows || j >= cols) return;
                if (board[i][j] == 'X') return;
                if (visited[i][j] == true) return;
                visited[i][j] = true;
                dfs(i+1, j);
                dfs(i-1, j);
                dfs(i, j+1);
                dfs(i, j-1);
            }

            // First pass to populate visited
            for (int r = 0; r < rows; r ++)
            {
                for (int c = 0; c < cols; c ++)
                {
                    if (r == 0 || c == 0 || r == rows - 1 || c == cols - 1) dfs(r, c);
                }
            }

            // Second pass to find non-visited 'O's
            for (int r = 0; r < rows; r ++)
            {
                for (int c = 0; c < cols; c ++)
                {
                    if (board[r][c] == 'O' && visited[r][c] == false) board[r][c] = 'X';
                }
            }
        }
    }

}