from heapq import heappush, heappop

# 50% runtime, 13% memory
# Well this is O(N log K) time and O(N) space lol
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        dict = {}
        for word in words:
            dict[word] = dict.get(word, 0) + 1
        heap = []
        for word in dict.keys():
            priority = dict[word] * 26 + (ord("z") - ord(word[0]))
            heappush(heap, (-priority, word))
        resp = []
        for _ in range(k):
            _, word = heappop(heap)
            resp.append(word)
        return resp
            
