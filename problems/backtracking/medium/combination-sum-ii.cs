namespace CombinationSumII
{
// All unique combinations to target
// Eih this is a very standard backtracking problem, but the C# IList syntax zzzzzzzzzz

    // Dang 85% runtime and 80% memory
    public class Solution_V3 {
        public IList<IList<int>> CombinationSum2(int[] candidates, int target) {
            var resp = new List<IList<int>>();
            Array.Sort(candidates);

            void recurse(int i, int cur_target, List<int> running_list)
            {
                if (cur_target < 0) 
                {
                    return;
                }
                else if (cur_target == 0)
                {
                    resp.Add(new List<int>(running_list));
                }
                else
                {
                    for (int j = i; j < candidates.Length; j ++)
                    {
                        if (j == i || candidates[j] != candidates[j - 1])
                        {
                            running_list.Add(candidates[j]);
                            recurse(j + 1, cur_target - candidates[j], running_list);
                            running_list.RemoveAt(running_list.Count - 1);
                        }
                    }
                }
                return;
            }

            recurse(0, target, new List<int>());
            return resp;
        }
    }


    public class Solution_V2 {
        public IList<IList<int>> CombinationSum2(int[] candidates, int target) {
            var resp = new List<IList<int>>();
            Array.Sort(candidates);

            void recurse(int i, int cur_target, List<int> running_list)
            {
                int cur_num = candidates[i];
                running_list.Add(cur_num);
                if (cur_target < 0)
                {
                }
                else if (cur_target == 0)
                {
                    resp.Add(new List<int>(running_list));
                }
                else
                {
                    for (int j = i + 1; j < candidates.Length; j ++)
                    {
                        if (j == i + 1 || candidates[j] != candidates[j - 1])
                        {
                            recurse(j, cur_target - candidates[j], running_list);
                        }
                    }
                }
                running_list.RemoveAt(running_list.Count - 1);
                return;
            }

            for (int i = 0; i < candidates.Length; i++)
            {
                if (i == 0 || candidates[i] != candidates[i - 1])
                {
                    recurse(i, target - candidates[i], new List<int>());
                }
            }

            return resp;
        }
    }

    // 68% runtime, 29% memory, implemented in 25 minutes in C#
    public class Solution {
        public IList<IList<int>> CombinationSum2(int[] candidates, int target) {
            var resp = new List<IList<int>>();
            Array.Sort(candidates);

            void recurse(int i, int prev_sum, List<int> running_list)
            {
                int cur_num = candidates[i];
                int new_sum = prev_sum + cur_num;
                running_list.Add(cur_num);
                if (new_sum > target)
                {
                }
                else if (new_sum == target)
                {
                    resp.Add(running_list.Select(x => x).ToList());
                }
                else
                {
                    for (int j = i + 1; j < candidates.Length; j ++)
                    {
                        if (j == i + 1 || candidates[j] != candidates[j - 1])
                        {
                            recurse(j, new_sum, running_list);
                        }
                    }
                }
                running_list.RemoveAt(running_list.Count - 1);
                return;
            }

            for (int i = 0; i < candidates.Length; i++)
            {
                if (i == 0 || candidates[i] != candidates[i - 1])
                {
                    recurse(i, 0, new List<int>());
                }
            }

            return resp;
        }
    }
}