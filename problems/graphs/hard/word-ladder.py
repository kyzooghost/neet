# All words of same length
# begin != end
# All words in wordList are unique

# Nodes are words
# Actually two-sided edge
# DFS from beginWord, can you get to endWord
# Two-sided edge - connect words that are one letter apart

# Efficient way to compute one letter apart?

from collections import defaultdict, deque

# Yay got first submission for Neetcode, 47 minutes, now time to get slaughtered by Leetcode
# Yep TLE at 23/51 cases for Leetcode
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # Avoid handling word outside of wordList
        wordList = [beginWord] + wordList
        
        visited = set()
        edges = defaultdict(list)

        # Fuck it, take the O(MN) time complexity here, M = length of word, N = len(wordList)
        def createEdge(i0, i1):
            word0, word1 = wordList[i0], wordList[i1]
            i = 0
            delta = 0
            while i < len(word0):
                if word0[i] != word1[i]: 
                    delta += 1
                if delta > 1: break
                i += 1
            # Early return if non-eligible
            if delta > 1: return
            edges[i0].append(i1)
            edges[i1].append(i0)

        foundEndWord = False
        j = 0
        while j < len(wordList):
            word = wordList[j]
            if word == endWord: foundEndWord = True
            for k in range(j-1, -1, -1): createEdge(j, k)
            j += 1
        # If endWord not in wordList, return 0
        if foundEndWord is False: return 0

        def recurse(index, step):
            word = wordList[index]
            # Basecase - found word
            if word == endWord: return step
            # Already visited
            if index in visited: return float("inf")
            visited.add(index)
            # DFS
            resp = float("inf")

            for next_index in edges[index]:
                resp = min(resp, recurse(next_index, step + 1))

            visited.remove(index)
            return resp

        res = recurse(0, 1)
        return res if res != float("inf") else 0

# Should use BFS, this will get the shortest path from beginWord
# Oooo still TLE but now 50/51 testcases passed
# Which comes back to my inefficient implementation for 'createEdge' hmm
class Solution_V2(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # Avoid handling word outside of wordList
        wordList = [beginWord] + wordList
        
        visited = set()
        edges = defaultdict(list)

        # Fuck it, take the O(MN^2) time complexity here, M = length of word, N = len(wordList)
        def createEdge(i0, i1):
            word0, word1 = wordList[i0], wordList[i1]
            i = 0
            delta = 0
            while i < len(word0):
                if word0[i] != word1[i]: 
                    delta += 1
                if delta > 1: break
                i += 1
            # Early return if non-eligible
            if delta > 1: return
            print(word0, word1)
            edges[i0].append(i1)
            edges[i1].append(i0)

        foundEndWord = False
        j = 0
        while j < len(wordList):
            word = wordList[j]
            if word == endWord: foundEndWord = True
            for k in range(j-1, -1, -1): createEdge(j, k)
            j += 1
        # If endWord not in wordList, return 0
        if foundEndWord is False: return 0

        queue = deque([0])
        resp = 0

        while queue:
            resp += 1
            queue_len = len(queue)
            for _ in range(queue_len):
                index = queue.popleft()
                word = wordList[index]
                if word == endWord: return resp
                visited.add(index)
                for next_index in edges[index]:
                    if next_index not in visited:
                        queue.append(next_index)
        return 0

# Alright the createEdge was O(M*N^2) time complexity previously
# I believe we can achieve O(M*N)
# Yay did it - 60% runtime, 45% memory
# Took 1 hr 24 mins and looking at a hint mmm
# Well, in my defence I am doing this on 1 hr of sleep lol
class Solution_V3(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # Avoid handling word outside of wordList
        wordList = [beginWord] + wordList
        
        visited = set()
        edges = defaultdict(list)

        # Base case
        foundEndWord = False
        for word in wordList: 
            if word == endWord: foundEndWord = True
        if foundEndWord is False: return 0
        
        j = 0
        # Iterate through each character - O(M)
        while j < len(beginWord):
            word_fragment_dict = defaultdict(list)
            # Iterate through each word - O(N) inner loop
            for k in range(0, len(wordList)):
                word = wordList[k]
                word_fragment = word[:j] + word[j+1:]
                # Preexisting match, create edge for each existing match
                if word_fragment in word_fragment_dict:
                    for existing_i in word_fragment_dict[word_fragment]:
                        edges[k].append(existing_i)
                        edges[existing_i].append(k)
                word_fragment_dict[word_fragment].append(k)
            j += 1

        queue = deque([0])
        resp = 0

        while queue:
            resp += 1
            queue_len = len(queue)
            for _ in range(queue_len):
                index = queue.popleft()
                word = wordList[index]
                if word == endWord: return resp
                visited.add(index)
                for next_index in edges[index]:
                    if next_index not in visited:
                        queue.append(next_index)
        return 0

# 68% runtime, 25% memory
class Solution_AfterNeet(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # Avoid handling word outside of wordList
        wordList = [beginWord] + wordList
        visited = set()
        edges = defaultdict(list)

        # Dang Python
        if endWord not in wordList: return 0
        
        # O(MN) create pattern -> word map
        # Interesting, not a conventional adjacency list, but everything with same pattern will have edge to each other
        patterns = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                patterns[pattern].append(word)
        
        queue = deque([beginWord])
        resp = 0
        while queue:
            resp += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord: return resp
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for next_word in patterns[pattern]:
                        if next_word not in visited:
                            visited.add(next_word)
                            queue.append(next_word)
        return 0

sln = Solution_AfterNeet()
print(sln.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))