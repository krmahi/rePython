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