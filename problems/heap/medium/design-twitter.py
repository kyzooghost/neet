
# See 10 most recent tweets in user news feed - pq hehe
# postTweet - New tweet with ID tweetId by user userId, will be made with unique tweetId
# getNewsFeed - Retrieve 10 most recent tweet Id - posted by followed, or user themselves. Ordered from most recent to least recent
# PQ for each user

# Most recent = biggest time

from collections import defaultdict

# 53% runtime, 97% memory done in 26 minutes
# This question is pretty annoying - First why is this categorized as a heap question? Spent 5-10 minutes trying to implement a heap solution
# But this ends up being very similar to the question I got for the Nethermind technical, it's actually a little harder
# Then I didn't know that set.remove(B) raises a KeyError if B doesn't exist in the set. It's happy to silently add, but not happy to silently remove lol
# Lol at Neet solution, I guess it's bounding the worst time complexity of getNewsFeed in exchange for ++complexity with a 'merge K-sorted list' approach
class Twitter(object):

    def __init__(self):
        # userId => following (includes self)
        self.follows = defaultdict(set)
        # stack -> (userId, tweetId)
        self.posts = []

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.follows[userId].add(userId)
        self.posts.append((userId, tweetId))

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        if userId not in self.follows: return []
        resp = []
        for i in range(len(self.posts) -1, -1, -1):
            posterId, tweetId = self.posts[i]
            if posterId in self.follows[userId]:
                resp.append(tweetId)
                if len(resp) >= 10: return resp
        return resp

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.follows[followerId].add(followerId)
        self.follows[followerId].add(followeeId)
        
    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        # Cannot unfollow yourself
        if followerId != followeeId and followerId in self.follows: self.follows[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

# twitter = Twitter()
# twitter.postTweet(1, 5)
# print(twitter.getNewsFeed(1))  
# twitter.follow(1, 2)
# twitter.postTweet(2, 6)
# print(twitter.getNewsFeed(1))  
# twitter.unfollow(1, 2)
# print(twitter.getNewsFeed(1))  