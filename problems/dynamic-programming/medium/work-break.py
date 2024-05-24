from typing import List

# Urgh ok watched Neet, using a trie to store the dict is the completely wrong direction
# Because the DP twist here is that dp[n] does not depend on dp[n-1], but dp[n - len(word)]. Yes you are jumping indexes. And because you are jumping indexes and not just using the last, you need O(N) storage and not O(1)
# Yea urgh, still doesn't feel intuitive to me because it's still a crazy brute force O(MNP) time complexity. Is it just because there is no more efficient way to solve this? Using a trie to do a single O(N) traversal just plain doesn't work. Then backtracking with a trie has some ridiculous time complexity and doesn't lend to memoization. Because if you go one character a time, it's a bit difficult to break it down into distinct repeating subtrees.
# But sigh, this is still 60% runtime and 56% memory...
class Solution_AfterWatchNeet:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        # O(N) where N = len(s)
        for i in range(len(s) - 1, -1, -1):
            # O(M) where M = len(wordDict)
            for word in wordDict:
                # O(P) where p = max word length
                
                # Out of bounds
                if i + len(word) > len(s):
                    continue
                # Substring match -> use dp array from previously
                if s[i:i+len(word)] == word:
                    if dp[i + len(word)]:
                        dp[i] = True
                        break
        return dp[0]

sln = Solution_AfterWatchNeet()
print(sln.wordBreak('leetcode', ["leet", "code"])) #T
print(sln.wordBreak('neetcode', ["neet", "code"])) #T
print(sln.wordBreak('applepenapple', ["apple", "pen"])) #T
print(sln.wordBreak('catsandog', ["cats","dog","sand","and","cat"])) #F
print(sln.wordBreak('catsincars', ["cats","cat","sin","in","car"])) #F
print(sln.wordBreak('aaaaaaa', ["aaaa","aaa"])) #T
print(sln.wordBreak('bb', ["a","b","bbb","bbbb"])) #T

class Trie(object):
    def __init__(self, isRoot = False):
        self.children = [None] * 26
        self.isWord = False
        self.isRoot = isRoot

    # Add words
    def insert(self, word):
        ptr = self
        for char in word:
            index = ord(char) - ord("a")
            if not ptr.children[index]:
                ptr.children[index] = Trie()
            ptr = ptr.children[index]
        ptr.isWord = True

# Sigh again, backtracking and greedy approach failed. Not sure what is the DP approach here?

# OK let's try a backtracking approach, still not sure how to DP this exactly
# Yep - TLE @ 35/46 cases on Leetcode, accepted on Neet lol
class Solution_V3:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Create trie
        self.trie = Trie(True)
        for word in wordDict:
            self.trie.insert(word)
        self.resp = False

        def dfs(s_index, ptr):
            # Pointer is nowhere
            if ptr is None:
                return
            # Reached end
            if s_index == len(s):
                self.resp = ptr.isWord or self.resp
                return
            
            # Found a word, reset to root node
            if ptr.isWord:
                dfs(s_index, self.trie)

            # Keep walking without reset to root node
            char_index = ord(s[s_index]) - ord("a")
            dfs(s_index + 1, ptr.children[char_index])

        dfs(0, self.trie)
        return self.resp

# Lol, this is just greedy on the opposite side - pass 35/46 cases
# So either way, greedy is failing here - "bb" and ["a","b","bbb","bbbb"]
class Solution_V2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie(True)
        ptr = trie

        for word in wordDict:
            trie.insert(word)
        
        for char in s:
            char_index = ord(char) - ord("a")
            if not ptr.children[char_index]:
                ptr = trie
                if not trie.children[char_index]:
                    return False
            ptr = ptr.children[char_index]

        return ptr.isWord



# Hmm, one solution is to insert every dict word into a trie, then keep walking along the trie
# O(26^max_word_length) space, O(N) time to traverse "s", and O(total character in dict) to create the trie. About linear time which is good
# An edge case is overlapping words hmm
# How could we DP this? It can't be based on wordDict, it must be based on position in 's'. I can't think of another way to do this, so let's just implement this
# Ok implemented this in 24 minutes - passed 36/46 test cases, but failed a testcase of "aaaaaaa" and ["aaaa","aaa"]. Well it is a greedy algorithm, greedy for the shortest length matching word
# What if we store all the possible substrings up to a position, then execute across each possibility? Seems like O(N^2) at least.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie(True)
        ptr = trie

        for word in wordDict:
            trie.insert(word)
        
        for char in s:
            char_index = ord(char) - ord("a")
            if not ptr.children[char_index]:
                return False
            ptr = ptr.children[char_index]
            # Reset to start
            if ptr.isWord: 
                ptr = trie

        return ptr.isRoot

# sln = Solution()
# print(sln.wordBreak('leetcode', ["leet", "code"])) #T
# print(sln.wordBreak('applepenapple', ["apple", "pen"])) #T
# print(sln.wordBreak('catsandog', ["cats","dog","sand","and","cat"])) #F
# print(sln.wordBreak('catsincars', ["cats","cat","sin","in","car"])) #F
# print(sln.wordBreak('aaaaaaa', ["aaaa","aaa"])) #T

