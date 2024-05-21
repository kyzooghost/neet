from typing import List
from collections import defaultdict

class Solution_Neet:
    def foreignDictionary(self, words: List[str]) -> str:
        # Edge case 1
        if len(words) == 1 and len(words[0]) == 1: return words[0]
        # Build adjacency list for each character
        adjacency = { c:set() for w in words for c in w}
        # Compare each word adjacent coupling
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLength = min(len(w1), len(w2))
            # Edge case 2
            if w1[:minLength] == w2[:minLength] and len(w1) > len(w2): return ""
            for j in range(minLength):
                if w1[j] != w2[j]:
                    adjacency[w1[j]].add(w2[j])
                    # Must stop once reached different character
                    break
        
        # False = visited, True = current path
        visited, stack = {}, []

        # Hmm, so first set visited = True, then visited = False
        # Normal return None, base case return visited[]
        # I think though, I can't remember this one as well as using a separate path variable
        def dfs(n1):
            if n1 in visited:
                return visited[n1]
            visited[n1] = True
            for n2 in adjacency[n1]:
                if dfs(n2): return True
            visited[n1] = False
            stack.append(n1)

        for c in adjacency.keys():
            if dfs(c): return ""

        resp = ""
        while stack:
            resp += stack.pop()
        return resp
    
# Jesus took 1.5 hrs - 1 hr of trying blind going into the wrong rabbit hole then 30 minutes with online hints
# Well have not done topological sort before, but that wasn't what got me stuck. It was that I went down the wrong rabbit hole with building the adjacency list.
# Ok big insights:
# 1.) Because words is already sorted, you only need to compare adjacent words
# 2.) Edge cases - Single word, ["wtfa", "wtf"] or same prefix must mean shorter word comes first, cycle in graph nodes
# 3.) How to do topological sort with cycle detection - Almost the exact same as DFS with cycle detection, but append to a stack at the same time you pop from the cycle path. Then pop the stack to get the topologically sorted nodes.

# Why does this kind of topological sort work?
# "Further back" nodes are higher on the stack, and the most nested node visited is the first on the stack
# So reversing this order with LIFO stack will get you a topological sort

class Solution_V1:
    def foreignDictionary(self, words: List[str]) -> str:
        # Alright the whole method of building the adjacency list is just wrong and too complicated, what if we just compare one word by one word?
        
        adjacency, letters = defaultdict(list), set()
        if len(words) == 1 and len(words[0]) == 1: return words[0]
        # Still O(len(words) * len(words[i])), but much easier to implement and reason through
        for i in range(len(words) - 1):
            cur_word, next_word = words[i], words[i + 1]
            min_length = min(len(cur_word), len(next_word))
            for j in range(min_length):
                letters.add(cur_word[j])
                if cur_word[j] != next_word[j]:
                    letters.add(next_word[j])
                    adjacency[cur_word[j]].append(next_word[j])
                    break
                if j == min_length - 1 and len(cur_word) > len(next_word): return ""
        stack, visited, path = [], {}, {}

        def dfs(n):
            visited[n] = True
            path[n] = True
            for i in adjacency.get(n, []):
                if i not in visited: 
                    if dfs(i): return True
                elif i in path: return True
            stack.append(n)
            del path[n]
            return False

        for i in letters:
            if i not in visited: 
                if dfs(i): return ""

        resp = ""
        while stack:
            resp += stack.pop()
        return resp

# Alright, I tried for an hour, not really getting anywhere. Best I did was pass 9/24 cases. The solution I came up with looks way too fragile to be a good solution hmm.
# Can only compare letter in the same index
# First letter gives us lots of info
# Represent letter as node, direction as order - h->e->r
# No result for topological sort -> if there is a cycle, so we need to detect for cycles as well

# Go through words and get all possible nodes + edges
    # First grouping - all, get from first letter
    # Second grouping - share 1st letter, get from 2nd letter
    # Third grouping - share 2nd letter, get from 3rd letter
    # Continue until either exceed max word length, or no words in groupings
    # O(len(words) * maxlen(words[i]))
# O(V+E) for DFS for cycle-find + topological sort - V is letters
# Detect if cycle
# If not -> return topological sort
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if not words:
            return ""
        i, groupings = 0, []
        adjacency = defaultdict(list)
        max_len = float("-inf")
        letters = set()

        # First letter
        cur_char = words[0][0]
        grouping = []

        # First pass O(N)
        for word in words:
            max_len = max(max_len, len(word))
            # New character and addition to adjacency list, split up grouping
            letters.add(word[i])
            if word[i] != cur_char:
                adjacency[cur_char].append(word[i])
                cur_char = word[i]
                if grouping: groupings.append(grouping)
                grouping = [word] if len(word) > i + 1 else []
            elif len(word) > i + 1:
                grouping.append(word)
        if grouping: groupings.append(grouping)
        i += 1

        while groupings and i < max_len:
            # new groupings
            new_groupings = []
            for group in groupings:
                # print(group)
                grouping = []
                cur_char = group[0][i]
                for word in group:
                    letters.add(word[i])
                    if word[i] != cur_char:
                        adjacency[cur_char].append(word[i])
                        cur_char = word[i]
                        if grouping: new_groupings.append(grouping)
                        grouping = [word] if len(word) > i + 1 else []
                    elif len(word) > i + 1:
                        grouping.append(word)
                if grouping: new_groupings.append(grouping)

            groupings = new_groupings
            i += 1
        
        visited, self.resp = {}, ""
        def dfs(n):
            visited[n] = True
            for i in adjacency.get(n, []):
                if i not in visited:
                    dfs(i)
            self.resp += n

        for letter in letters:
            if letter not in visited:
                dfs(letter)

        if not adjacency:
            if len(letters) == 1:
                return letters.pop()
            else:
                return ""

        return self.resp[::-1]

sln = Solution_Neet()
print(sln.foreignDictionary(["z","o"]))
print(sln.foreignDictionary(["hrn","hrf","er","enn","rfnn"]))
print(sln.foreignDictionary(["z","z"]))
print(sln.foreignDictionary(["wrtkj","wrt"]))
print(sln.foreignDictionary(["aaa","aa", "a"]))
print(sln.foreignDictionary(["z"]))
words = ["abcdefgh","bdefghij","cghij","dfghij","efghij","fghij","ghij","hij","ij","j","abcdefghi","bdefghijk","cghijk","dfghijk","efghijk","fghijk","ghijk","hijk","ijk","jk","k"]
print(sln.foreignDictionary(words))

