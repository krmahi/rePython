import heapq
from collections import defaultdict

#sorting: time -> O(n * m + tlogt) + O(1) space -> O(N * m + N * m) => N = userId, M = followeeID, m = tweets 
class Twitter:
    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, UserId, TweetId):
        self.tweetMap[UserId].append([self.time, TweetId])
        self.time += 1

    def getFeed(self, UserId):
        feed = self.tweetMap[UserId][:]

        for followeeId in self.followMap[UserId]:
            feed.extend(self.tweetMap[followeeId])
        
        feed.sort(key=lambda x: -x[0])
        return [tweetId for _, tweetId in feed[:10]]
    
    def follow(self, followerId, followeeId):
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def Unfollow(self, followerId, followeeId):
        self.followMap[followerId].discard(followeeId) # discard dosent throw any error if item not in set 

#heap instead of normal sorting
class Twitter:
    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, UserId, TweetId):
        self.tweetMap[UserId].append([self.time, TweetId])
        self.time += 1

    def getFeed(self, UserId):
        feed = self.tweetMap[UserId][:]

        for followeeId in self.followMap[UserId]:
            feed.extend(self.tweetMap[followeeId])
        
        return [tweetId for _, tweetId in heapq.nlargest(10, feed, key=lambda x: x[0])]
    
    def follow(self, followerId, followeeId):
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def Unfollow(self, followerId, followeeId):
        self.followMap[followerId].discard(followeeId) # discard dosent throw any error if item not in set 

# heap optimised -> time: O(1) + O(k) + O(10.logk) => O(1) + O(k)
class Twitter:
    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, UserId, TweetId):
        self.tweetMap[UserId].append([self.time, TweetId])
        self.time -= 1

    def getFeed(self, UserId):
        # time -> O(10*logk) + O(k) => O(k) || k -> no. of followeeId 
        res = []
        minHeap = []

        self.follow(UserId, UserId)
        for followeeId in self.followMap[UserId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([time, tweetId, followeeId, index - 1])
        
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            
            if index <= 0:
                time, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush([time, tweetId, followeeId, index - 1])

        return res 
    
    def follow(self, followerId, followeeId):
        self.followMap[followerId].add(followeeId)

    def Unfollow(self, followerId, followeeId):
        self.followMap[followerId].discard(followeeId) # discard dosent throw any error if item not in set 
