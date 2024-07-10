
// Wow...I actually got 61/65 test cases with TLE on my first submission in C#
// I had the idea already within 6ish minutes, but fuarkkkk I'm finding the Dictionary API so painful compared to Python
// So ended up getting first submission at ~35 minutes. Would have chunked out in 20 minutes in Python.
// This ...TryGetValue -> out pattern urgh. In Python it would just be 'if x in dict' zzzz
// 17% runtime, 74% memory, lol missed a DFS edge case, gg. 
namespace DistinctSubsequences 
{

    // Much simpler 20% runtime, 70% memory
    public class Solution_V2 {
        public int NumDistinct(string s, string t) 
        {
            if (s.Length < t.Length) return 0;
            int[,] dp = new int[t.Length, s.Length];
            for (int i = 0; i < t.Length; i++) {
                for (int j = 0; j < s.Length; j++) {
                    dp[i, j] = -1;
                }
            }

            int recurse(int s_i, int t_i)
            {
                if (t_i == t.Length) return 1;
                if (s_i == s.Length) return 0;
                if (dp[t_i, s_i] != -1) return dp[t_i, s_i];
                
                int resp = 0;
                
                // Progress current t_i
                if (s[s_i] == t[t_i]) resp += recurse(s_i + 1, t_i + 1);
                // Don't progress current t_i. If match, means you reject this match.
                resp += recurse(s_i + 1, t_i);

                dp[t_i, s_i] = resp;
                return resp;
            }

            return recurse(0, 0);
        }
    }

    public class Solution {
        public int NumDistinct(string s, string t) {
            if (s.Length < t.Length) return 0;

            Dictionary<char, List<int>> char_to_s_positions = new Dictionary<char, List<int>>();
            for (int i = 0; i < s.Length; i++)
            {
                char s_char = s[i];
                if (char_to_s_positions.TryGetValue(s_char, out List<int> s_char_list)) 
                {
                    s_char_list.Add(i);
                }
                else
                {
                    char_to_s_positions.Add(s_char, new List<int>() {i});
                }
            }

            // t_i, s_i -> num
            Dictionary<(int, int), int> dp = new Dictionary<(int, int), int>();

            int dfs(int t_i, int s_i) 
            {
                // Seen in DP before
                if (dp.TryGetValue((t_i, s_i), out int dp_val)) 
                {
                    return dp_val;
                }

                // If remaining_s < remaining_t, not possible
                int remaining_s = s.Length - 1 - s_i;
                int remaining_t = t.Length - 1 - t_i;
                if (remaining_s < remaining_t) return 0;

                // Reached end
                if (t_i == t.Length - 1) 
                {
                    dp.Add((t_i, s_i), 1);
                    return 1;
                }

                int resp = 0;
                char next_t_char = t[t_i + 1];

                if (char_to_s_positions.TryGetValue(next_t_char, out List<int> next_s_indexes))
                {
                    foreach (int next_s_i in next_s_indexes)
                    {
                        if (next_s_i > s_i) resp += dfs(t_i + 1, next_s_i);
                    }
                }

                dp.Add((t_i, s_i), resp);
                return resp;
            }

            int resp = 0;
            if (char_to_s_positions.TryGetValue(t[0], out List<int> s_indexes))
            {
                foreach (int s_i in s_indexes)
                {
                    resp += dfs(0, s_i);
                }
            }
            else 
            {
                return 0;
            }

            return resp;
        }
    }
}
