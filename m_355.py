import heapq

class Twitter:

    def __init__(self):
        self.tweets_by_uid = {}
        self.followers_by_uid = {}
        self.my_tweets_by_uid = {}
        self.t_stamp = 0

    def get_t_stamp(self):
        ret = self.t_stamp
        self.t_stamp -= 1
        return ret

    def postTweet(self, userId: int, tweetId: int) -> None:
        ts = self.get_t_stamp()
        followers = list(self.followers_by_uid.get(userId, {}).keys())
        followers.append(userId)
        for f in followers:
            t = self.tweets_by_uid.get(f, [])
            if not t:
                self.tweets_by_uid[f] = t
            heapq.heappush(self.tweets_by_uid[f], (ts, tweetId))
        my_t = self.my_tweets_by_uid.get(userId, [])
        if not my_t:
            self.my_tweets_by_uid[userId] = my_t
        heapq.heappush(my_t, (ts, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        t = self.tweets_by_uid.get(userId, [])
        ret = []
        t.sort(key=lambda x: x[0])
        return list(map(lambda x: x[1], t[:10]))
        print(self.tweets_by_uid)

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        f = self.followers_by_uid.get(followeeId, {})
        if not f:
            self.followers_by_uid[followeeId] = f

        if followerId in f:
            return

        f[followerId] = True

        my_t = self.my_tweets_by_uid.get(followeeId, [])
        nf = self.tweets_by_uid.get(followerId, [])
        if not nf:
            self.tweets_by_uid[followerId] = nf

        for t in my_t:
            heapq.heappush(nf, t)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        self.followers_by_uid.get(followeeId, {}).pop(followerId, None)

        my_t = list(map(lambda x: x[1], self.my_tweets_by_uid.get(followeeId, [])))
        nf = self.tweets_by_uid.get(followerId, [])
        new_nf = []
        self.tweets_by_uid[followerId] = new_nf

        for i in range(len(nf)):
            if nf[i][1] not in my_t:
                heapq.heappush(new_nf, nf[i])


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
