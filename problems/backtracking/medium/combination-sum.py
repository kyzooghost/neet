# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

class Solution_Neet(object):
    # 16% runtime, 77% memory
    # Hmm, ok so you did have to reduce this to a recursive call, but I wasn't able to reduce this to just two more recursive calls inside the recursive function
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        resp = []

        def dfs(i, cur_combination, running_total):
            if running_total == target:
                resp.append(list(cur_combination))
                return
            if i >= len(candidates) or running_total > target:
                return
            
            # First choice - Add self
            new_combination = tuple(list(cur_combination) + [candidates[i]])
            dfs(i, new_combination, running_total + candidates[i])
            # Second choice - Add nothing, and move to next candidate
            # Don't have to directly add next candidate, because this can be done in next DFS step
            # Also if directly add next candidate, how can you consider to skip the candidate?
            dfs(i + 1, cur_combination, running_total)

        dfs(0, (), 0)
        return resp


class Solution_V2(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        resp = []
        
        # num - current num being considered
        # candidate_combination - tuple of nums
        # new_target - new target
        def recurse(i, candidate_combination, new_target):
            if i >= len(candidates):
                return
            num = candidates[i]
            if num > new_target:
                return
            # Found eligible combination
            elif num == new_target:
                combination = list(candidate_combination) + [num]
                resp.append(combination)
            else:
                quotient = target // num
                print(quotient)
                for j in range(1, quotient + 1):
                    # Found eligible combination
                    if j * num == new_target:
                        combination = list(candidate_combination) + [num] * j
                        resp.append(combination)
                    # Recurse into next largest number
                    elif j * num > new_target:
                        pass
                    else:
                        next_candidate_combination = tuple(list(candidate_combination) + [num] * j)
                        next_new_target = new_target - j * num
                        for next_index in range(i + 1, len(candidates)):
                            recurse(next_index, next_candidate_combination, next_new_target)

        for i in range(len(candidates)):
            recurse(i, (), target)

        return resp


class Solution_V1(object):
    # Here I want to make an new list containing all possible multiples
    # Then find the combinations within the new list
    # Urgh got to 120/160 testcases passing, in 45 minutes, but the frozenset is acting up - two different frozensets appear to have a hash collision as a dict key
    # Also, got mucked about by .append and .extend list methods - they don't return anything and act in place. If you want to return something, use + syntax
    # Urgh, didn't realise - you can't use a set because we are dealing with duplicate values
    # Also urgh, took ~1.5-2 hrs to come up with a working solution, after multiple failed attempts
    # combination_set is unneccesary because the order in which we consider numbers, mean we are always considering a new combination
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        resp = []
        
        # O (N lg N)
        candidates.sort()
        trimmed_candidates = []

        for num in candidates:
            if num < target:
                trimmed_candidates.append(num)
            elif num == target:
                resp.append([num])
            else:
                pass

        # num -> index (trimmed candidates)
        dict = {}
        for i, num in enumerate(trimmed_candidates):
            dict[num] = i
        
        # num - current num being considered
        # candidate_combination - tuple of nums
        # new_target - new target
        def recurse(num, candidate_combination, new_target):
            if num > new_target:
                return
            # Found eligible combination
            elif num == new_target:
                combination = list(candidate_combination) + [num]
                resp.append(combination)
            else:
                quotient = target // num
                for i in range(1, quotient + 1):
                    # Found eligible combination
                    if i * num == new_target:
                        combination = list(candidate_combination) + [num] * i
                        resp.append(combination)
                    # Recurse into next largest number
                    elif i * num > new_target:
                        pass
                    else:
                        index = dict[num]
                        next_candidate_combination = tuple(list(candidate_combination) + [num] * i)
                        next_new_target = new_target - i * num
                        for next_index in range(index + 1, len(trimmed_candidates)):
                            next_number = trimmed_candidates[next_index]
                            recurse(next_number, next_candidate_combination, next_new_target)

        for num in trimmed_candidates:
            recurse(num, (), target)

        return resp
        

s = Solution_V1()
print(s.combinationSum([7,3,2], 18))

class Solution(object):
    # Umm, is this 1-sum, 2-sum, 3-sum all rolled into one question?
    # It's tricky that the same number can be chosen multiple times
    # All elements of candidates are distinct hmm...
    # They limit candidates.length significantly, so must mean they don't expect a very time efficient solution
    # Ok took 33 minutes to come up with this solution, passing 83/160 cases
    # I don't think this is the correct track though, because it can't deal with multiples of more than one number
    # We should use the constraint that there are no negative numbers
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        resp = []

        # O (N lg N)
        candidates.sort()

        # num -> Y
        dict, combinations = {}, {}
        for num in candidates:
            dict[num] = True

        # Loop through all candidates
        for num in candidates:
            if target < num:
                pass
            elif target == num:
                resp.append([num])
            else:
                quotient = target // num
                # Loop through repeat occurence for each candidate
                for i in range(1, quotient + 1):
                    new_target = target - i * num
                    if new_target == 0:
                        combination = [num] * i
                        if tuple(combination) not in combinations:
                            combinations[tuple(combination)] = True
                            resp.append(combination)
                    # Find single match
                    elif new_target in dict:
                        combination = [num] * i
                        combination.append(new_target)
                        if tuple(combination) not in combinations:
                            combinations[tuple(combination)] = True
                            resp.append(combination)

        return resp