
// The thing is, once you move down, you can never move up again
// You can use the same algorithm for robot 1 and 2
// At each step, only two choices - right or down
// Compare sum of two rows, choose bigger with bias to top
// top vs bottom counters - O(N) to count. Update counters and compare at each move

// 33% runtime, 50% memory in 39 minutes
// Sigh...really lost my touch with these LC questions zzz
// I had the correct idea, but I didn't recognise that R1 is playing a different game from R2
// R1 is playing denial, not collecting maximum
// It's two separate algorithms for going through the board zzz
function gridGame(grid: number[][]): number {
    const cols = grid[0].length;

    function playR1Round() {
        // Create top & bottom ptr
        let top = 0;
        let bottom = grid[1][0];
        for (let i = cols - 1; i >= 1; i--) {
            top += grid[0][i]
        }

        // Start game
        let r = 0;
        let c = 0;

        while (r <= 1 && c <= cols - 1) {
            grid[r][c] = 0;

            // Reached end
            if (r == 1 && c == cols - 1) break;
            // Must move right
            else if (r == 1) c += 1
            // Must move down
            else if (c == cols - 1) r += 1
            // Or have choice
            else {
                // Move right
                if (top >= bottom) {
                    c += 1;
                    top -= grid[r][c]
                    bottom += grid[r+1][c]
                // Move down - no need to update ptrs
                } else {
                    r += 1;
                }
            }
        }

    }

    function playR2Round() {
        // Create top & bottom ptr
        let resp = 0;
        let top = 0;
        let bottom = grid[1][0];
        for (let i = cols - 1; i >= 1; i--) {
            top += grid[0][i]
            bottom += grid[1][i]
        }

        // Start game
        let r = 0;
        let c = 0;

        while (r <= 1 && c <= cols - 1) {
            resp += grid[r][c];
            grid[r][c] = 0;

            // Reached end
            if (r == 1 && c == cols - 1) break;
            // Must move right
            else if (r == 1) c += 1
            // Must move down
            else if (c == cols - 1) r += 1
            // Or have choice
            else {
                // Move right
                if (top >= bottom) {
                    top -= grid[r][c+1]
                    bottom -= grid[r+1][c]
                    c += 1;
                // Move down - no need to update ptrs
                } else {
                    r += 1;
                }
            }
        }

        return resp;
    }

    playR1Round();
    const r2 = playR2Round();
    return r2;
};

// const grid = [[2,5,4],[1,5,1]];
// const grid = [[3,3,1],[8,5,2]];
// const grid = [[1,3,1,15],[1,3,3,1]];
const grid = [[20,3,20,17,2,12,15,17,4,15],[20,10,13,14,15,5,2,3,14,3]];
console.log(gridGame(grid));