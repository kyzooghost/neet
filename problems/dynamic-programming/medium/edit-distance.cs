
// Can insert, delete, replace character
// How is this a DP problem? What is the decision tree?
// Same # of operations from word1 to word2, and visa versa, since all operations have reverse available

// Dang 43 minutes for first submission, and got wrong answer at 1022/1146 testcases
// Lol found the bug, and got 26% runtime, 66% memory at 51 minutes haha
// Dang Console.WriteLine() has a lot of overhead - makes it 5% runtime and 6% memory
// Yay for getting this by myself at 12AM and sleep deprived lol, but eih I didn't find easy enough to be a medium
// Working out that recursive function took me ages, I had to draw out the logic for each line and didn't get any 'quick jumps' other than having seen character-by-character 2D DP problems before
namespace EditDistance
{
    // Slight improvement in that you can be greedy in the matching character case and assume pass - because this will definnitely result in minimum distance
    // 37% runtime, 66% memory
    // Still harder problem than the last two 'hard' 2D DP problems though
    public class Solution_V2 {
        public int MinDistance(string word1, string word2) {
                int[,] dp = new int[word1.Length, word2.Length];
                for (int i = 0; i < word1.Length; i++) {
                    for (int j = 0; j < word2.Length; j++) {
                        dp[i,j] = -1;
                    }
                }
                int MaxLength = Math.Max(word1.Length, word2.Length);

                // Pass, delete, insert, replace
                int recurse(int i, int j) 
                {
                    // End of word2 - must delete remainder of word1
                    if (j == word2.Length) return word1.Length - i;
                    // End of word1 - must insert remainder of word2
                    if (i == word1.Length) return word2.Length - j;
                    if (dp[i, j] != -1) return dp[i, j];

                    int resp = MaxLength;
                    // Pass
                    if (word1[i] == word2[j]) {
                        resp = Math.Min(resp, 0 + recurse(i + 1, j + 1));
                    // Replace (mutually exclusive)
                    } else {

                        // Delete
                        resp = Math.Min(resp, 1 + recurse(i + 1, j));
                        resp = Math.Min(resp, 1 + recurse(i + 1, j + 1));

                        // Insert before
                        resp = Math.Min(resp, 1 + recurse(i, j + 1));
                    }

                    dp[i, j] = resp;
                    return resp;
                }
                
                return recurse(0, 0);
        }
    }


    public class Solution {
        public int MinDistance(string word1, string word2) {
            int[,] dp = new int[word1.Length, word2.Length];
            for (int i = 0; i < word1.Length; i++) {
                for (int j = 0; j < word2.Length; j++) {
                    dp[i,j] = -1;
                }
            }

            // Pass, delete, insert, replace
            int recurse(int i, int j) 
            {
                // End of word2 - must delete remainder of word1
                if (j == word2.Length) return word1.Length - i;
                // End of word1 - must insert remainder of word2
                if (i == word1.Length) return word2.Length - j;
                if (dp[i, j] != -1) return dp[i, j];

                // Delete
                int resp = 1 + recurse(i + 1, j);

                // Pass
                if (word1[i] == word2[j]) {
                    resp = Math.Min(resp, 0 + recurse(i + 1, j + 1));
                // Replace (mutually exclusive)
                } else {
                    resp = Math.Min(resp, 1 + recurse(i + 1, j + 1));
                }

                // Insert before
                resp = Math.Min(resp, 1 + recurse(i, j + 1));

                dp[i, j] = resp;
                return resp;
            }
            
            return recurse(0, 0);
        }
    }  
}